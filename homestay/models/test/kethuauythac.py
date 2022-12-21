from odoo import models, fields


class kethua(models.Model):
    _name= 'aaakethua'
    _inherits = {'aaauythac':'uythac'}
    
    
    phone = fields.Char(string='sdt')
    