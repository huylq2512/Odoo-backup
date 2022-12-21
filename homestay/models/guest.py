from odoo import fields, models

class guest(models.Model):
        _name = "aaguest"
        _description = "information guest"

        
        name = fields.Char(string="Họ tên khách hàng")
        phone = fields.Char(string ="Số điện thoại")
        front_card = fields.Binary(string="Ảnh CCCD/CMND mặt trước")
        back_card = fields.Image(string="Ảnh CCCD/CMND mặt sau", max_width=1, max_height=1)
        booking_id = fields.One2many('aabooking', 'guest_ids', string='Danh sách phòng đặt')
        invoice_id = fields.One2many('aainvoice', 'guest_id', string='Danh sách hoá đơn')