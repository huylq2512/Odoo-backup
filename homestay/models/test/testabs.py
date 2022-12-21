from odoo import fields, models,api


class testabs(models.AbstractModel):
    _name = 'aatestabs'
    _auto = True
    
    name = fields.Char(string='Char')
    