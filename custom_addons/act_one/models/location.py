from odoo import models, fields

class Location(models.Model):
    _name = "location"

    name = fields.Char()
    code = fields.Integer()