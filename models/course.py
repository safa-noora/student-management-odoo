from odoo import models,fields

class Course(models.Model):
	_name='student.management.course'
	_description='Course'

	name=fields.Char(required=True)
	student_ids=fields.Many2many('student.management.student',string='Students')