from odoo import models,fields
class StudentInherit(models.Model):
	_inherit="student.management.student"
	phone=fields.Char()
	age = fields.Integer(required=True)
	email = fields.Char(required=True)

