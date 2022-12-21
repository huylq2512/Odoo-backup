from odoo import models, fields


class Service(models.Model):
    _name = 'aaservice'
    _description = "Services offered"
    
    name = fields.Char(string="Tên dịch vụ")
    price = fields.Integer(string="Giá")
    type = fields.Selection([
        ('Dọn Dẹp', 'dọn dẹp'),
        ('Ăn Uống', 'ăn uống'),
        ('Giặt Giũ', 'giặt giũ')
          ], string="Các loại dịch vụ")
    
    # atest = fields.Many2many('aroom', 'atesst')
