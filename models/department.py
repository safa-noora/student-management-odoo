from odoo import models, fields

class Department(models.Model):
    _name = 'student.management.department'
    _description = 'Department'

    name = fields.Char(required=True)
    student_ids=fields.One2many('student.management.student','department_id')