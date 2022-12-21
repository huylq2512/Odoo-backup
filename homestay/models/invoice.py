from odoo import fields, models, api


class Invoice(models.Model):
    _name = "aainvoice"
    _rec_name = "guest_id"
    
    name = fields.Char(string="Mã hoá đơn")
    guest_id = fields.Many2one(comodel_name="aaguest", string='Tên Khach Hang', ondelete='restrict', required=True)
    booking_id = fields.One2many('aabooking', 'invoice_ids', string='Danh sách hoá đơn')
    service = fields.One2many('aaroom.service', 'invoice_ids', string='Danh sách dich vu')
    status = fields.Boolean(string='Thanh Toán', default=False)
    sum_price_room = fields.Float(string="Tong tien Phong")
    sum_price_service = fields.Float(string="Tong tien Dich Vu")
    sum_price = fields.Float(string="Tong tien Phai Tra")
    test_soluong = fields.Integer(string='test nhaaa')
    
    @api.onchange('guest_id')
    def _get_booking(self):
        if self.guest_id:
            a = self.env["aabooking"].search_count([('guest_ids.name', '=', self.guest_id.name),('status', '=', False)])
            self.test_soluong = a
                
    @api.onchange('guest_id')
    def _get_booking_in_guest(self):
        if self.guest_id:
            a = self.env["aabooking"].search([('guest_ids.name', '=', self.guest_id.name),('status', '=', False)])
            self.booking_id = a
                
    @api.onchange('guest_id')
    def sum_pricee(self):
        if self.guest_id:
            a = self.env["aabooking"].search([('guest_ids.name', '=', self.guest_id.name)])
            b = a.mapped('room_pice')
            temp = 0
            for rec in b:
                temp += rec
            self.sum_price_room = temp
            temp_service = 0
            for record in self.booking_id.room_ids:
                d = self.env["aaroom.service"].search([('room_id', '=', record.id)])
                if d.price_service > 0:
                    temp_service += d.price_service
                else: 
                    pass
            self.sum_price_service = temp_service
            self.sum_price = temp + temp_service

    def acction(self):
         a = self.env["aabooking"].search([('guest_ids.name', '=', self.guest_id.name)])
         for i in a:
             i.status = True
             print(i.status)
             i.room_ids.status = False
         self.status = True
    

