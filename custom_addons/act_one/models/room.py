from odoo import models, fields

class Room(models.Model):
    _name = "room"

    name = fields.Char(required=True)
    code = fields.Integer(required=True)

    active = fields.Boolean('Active', default=True)