from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Registration(models.Model):
    _name = 'registration'
    _description = 'Course Registration'

    trainee_id = fields.Many2one(
        'res.users', 
        string='Trainee Name', 
        required=True,
        default=lambda self: self.env.user 
    )

    course_id = fields.Many2one('course', string='Course Name', required=True)

    course_description = fields.Text(related='course_id.description', string='Course Description', readonly=True)
    start_date = fields.Date(related='course_id.start_date', string='Start Date', readonly=True)
    end_date = fields.Date(related='course_id.end_date', string='End Date', readonly=True)
    number_of_days = fields.Integer(related='course_id.number_of_days', string='Number of Days', readonly=True)
    time = fields.Float(related='course_id.time', string='Time', readonly=True)

    #relations
    teacher_id = fields.Many2one(related='course_id.teacher_id', string='Teacher Name', store=True)
    room_id = fields.Many2one(related='course_id.room_id', string='Room Number', readonly=True)
    location_id = fields.Many2one(related='course_id.location_id', string='Course Location', readonly=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('teacher', 'Teacher Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', required=True, tracking=True)

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise UserError("Only draft registrations can be confirmed.")
            record.state = 'teacher'

    def action_approve(self):
        for record in self:
            if record.state != 'teacher':
                raise UserError("Only registrations in Teacher Review can be approved.")
            record.state = 'approved'

    def action_reject(self):
        for record in self:
            if record.state != 'teacher':
                raise UserError("Only registrations in Teacher Review can be rejected.")
            record.state = 'rejected'
