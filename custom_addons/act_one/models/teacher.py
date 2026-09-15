from odoo import models, fields

class Teacher(models.Model):
    _name = "teacher"

    name = fields.Char()
    code = fields.Integer()