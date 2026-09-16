from odoo import models, fields

class Teacher(models.Model):
    _name = "teacher"

    name = fields.Char(required=True)
    code = fields.Integer(required=True)

    #relations
    user_id = fields.Many2one('res.users', string='Related User')