from odoo import models, fields

class Registration(models.Model):
    _name = "registration"

    trainee_name = fields.Char()
    course_name = fields.Char()
    course_description = fields.Text()
    teacher_name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    number_of_days = fields.Integer()
    time = fields.Float()
    room_number = fields.Integer()
    course_location = fields.Char()
