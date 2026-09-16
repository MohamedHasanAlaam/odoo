from odoo import models, fields

class Location(models.Model):
    _name = "location"

    name = fields.Char(required=True)
    code = fields.Integer(required=True)