# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InvoiceWizard(models.TransientModel):
    _name = "aainvoice.winzad"
    
    name = fields.Char(string='a')
    guest_id = fields.Many2one(comodel_name="aaguest", string='Tên Khach Hang', ondelete='restrict', required=True)
    
    def multi_update_author_id(self):
       print('hello')
       pass
    
    
