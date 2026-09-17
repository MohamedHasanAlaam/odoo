from odoo import models, fields, api

class Location(models.Model):
    _name = "location"

    name = fields.Char(required=True)
    code = fields.Char(readonly=True, default='New')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('code', 'New') == 'New':
                vals['code'] = self.env['ir.sequence'].next_by_code('location.code.seq') or 'New'
        return super(Location, self).create(vals_list)