from odoo import models, fields


class uythac(models.Model):
    _name = 'aaauythac'
    
    name = fields.Char(string='name')
    age = fields.Integer(string='age')
    address = fields.Char(string='address')
    uythac = fields.Many2one('aaakethua', ondelete='restrict')