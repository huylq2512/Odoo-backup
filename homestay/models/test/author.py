from odoo import fields, models

class Author(models.Model):
    _name = "aauthor"
    
    name = fields.Char(string='Tên Chủ Sở Hữu')
    number_phone = fields.Char(string='Số điện thoại')
    card_id = fields.Char(string='CCCD')
    homes_id = fields.One2many("aahome", 'author_id', string='Homestay sở hữu')