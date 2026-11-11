from odoo import models, fields,api
from odoo.exceptions import UserError,ValidationError


class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(required=True)
    age = fields.Integer(default=18)
    email = fields.Char()
    date_of_birth = fields.Date()
    course_fees = fields.Float()
    registration_fees=fields.Float()
    total_fees=fields.Float(compute='_compute_total_fees',store=True)
    active = fields.Boolean(default=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    department_id = fields.Many2one('student.management.department')
    state = fields.Selection([
        ('new', 'New'),
        ('active', 'Active'),
        ('graduated', 'Graduated'),
    ], required=True, copy=False, default='new')
    course_ids=fields.Many2many('student.management.course',string='Courses')

    def action_confirm_admission(self):
        for student in self:
            if student.state != 'new':
                raise UserError("Only new students can be admitted.")

            student.write({'state': 'active'})

    def action_graduate(self):
        for student in self:
            if student.state != 'active':
                raise UserError("Only active students can be graduated.")

            student.write({'state': 'graduated'})


    @api.constrains('age')
    def check_age(self):
        for student in self:
            if student.age < 0:
                raise ValidationError("Age cannot be negative.")

    
    @api.onchange('age')
    def onchange_age(self):
        if self.age < 18:
            return{
                'warning': {
                 'title': 'Age Warning',
                 'message': 'Student must be at least 18 years old.'
                 }
           }
    @api.depends('course_fees','registration_fees')
    def _compute_total_fees(self):
        for student in self:
            student.total_fees=(
               student.course_fees+student.registration_fees 
            )