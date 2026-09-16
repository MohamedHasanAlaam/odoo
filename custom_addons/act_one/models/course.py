from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = "course"

    # attributes
    name = fields.Char(required=True)
    description = fields.Text(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    
    number_of_days = fields.Integer(
        string='Number of Days', 
        compute='_compute_number_of_days', 
        store=True
    )

    time = fields.Float(required=True)
    available_seats = fields.Integer(required=True)
    target_gender = fields.Selection([
        ('male', 'Male'),   
        ('female', 'Female')
        ], required=True)
    deadline = fields.Date(required=True)

    active = fields.Boolean('Active', default=True)
    
    #relations
    teacher_id = fields.Many2one('teacher', string='Teacher Name')
    room_id = fields.Many2one('room', string='Room Number')
    location_id = fields.Many2one('location', string='Course Location')

    @api.depends('start_date', 'end_date')
    def _compute_number_of_days(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                
                if delta.days >= 0:
                    record.number_of_days = delta.days + 1
                else:
                    record.number_of_days = 0
            else:
                record.number_of_days = 0

    @api.constrains('start_date', 'end_date')
    def _check_date_sanity(self):
        for record in self:
            if record.start_date and record.end_date and record.end_date < record.start_date:
                raise ValidationError("The end date cannot be earlier than the start date.")