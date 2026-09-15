from odoo import models, fields

class Courses(models.Model):
    _name = "courses"

    name = fields.Char()
    description = fields.Text()
    teacher_name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    number_of_days = fields.Integer()
    time = fields.Float()
    room_number = fields.Integer()
    course_location = fields.Char()
    available_seats = fields.Integer()
    target_gender = fields.Selection([
        ('male', 'Male'),   
        ('female', 'Female')
        ])
    deadline = fields.Date()