from odoo import models, fields, api

class Room(models.Model):
    _name = "room"

    name = fields.Char(required=True)
    code = fields.Char(readonly=True, default='New')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', 'New') == 'New':
                vals['code'] = self.env['ir.sequence'].next_by_code('room.code.seq') or 'New'
        return super(Room, self).create(vals_list)