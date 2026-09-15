from odoo import models, fields

class Room(models.Model):
    _name = "room"

    name = fields.Char()
    code = fields.Integer()