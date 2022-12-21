from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import *


class Booking(models.Model):
    _name = "aabooking"
    _description = "information booking"
    
    name = fields.Char(string="Mã Đơn", compute="_identity_name", store=True)
    checkin = fields.Datetime(string='Thời gian lấy phòng', default=fields.Datetime.now(), readonly=True)
    checkout = fields.Datetime(string='Thời gian trả phòng')
    status = fields.Boolean(string='Trang Thai', readonly=True)
    duration = fields.Float(string='Số thời gian ở', digits=(2, 10))
    time_stay = fields.Integer(string="Số ngày ở")
    room_pice = fields.Float(string='Giá Phòng', compute="_get_price_room", store=True)
    guest_ids = fields.Many2one(comodel_name="aaguest", string='Tên Khách Hàng', ondelete='restrict', required=True)
    room_ids = fields.Many2one(comodel_name="aaroom", string='Tên Phòng', ondelete='restrict', required=True, domain=[('status', '=', False)])
    invoice_ids = fields.Many2one(comodel_name="aainvoice", string='invoice test', ondelete='restrict')
    
    @api.depends('room_ids', 'time_stay')
    def _get_price_room(self):
        for record in self:
            if record.room_ids:
                record.room_pice = record.room_ids.price * record.time_stay
                if record.room_pice == 0:
                    record.room_pice = record.room_ids.price
            else:
                record.room_pice = 150000

    @api.constrains('checkout')
    def _checkin_not_later_than_checkout(self):
        for i in self:
            if i.checkout:
                if i.checkin <= i.checkout:
                    pass
                else:
                     raise ValidationError("Thời gian checkin không thể lớn hơn thời gian checkout")
            else:
                pass
    
    @api.depends('guest_ids', 'room_ids')
    def _identity_name(self):
        for record in self:
            record.name = "Booking" + str(record.guest_ids.id) + str(record.room_ids.id)
            
    @api.constrains('checkout')
    def _not_booking_duplicate(self):
        for i in self:
            time_stay = self.env['aabooking'].search([('name', '=', i.name), ('id', '!=', i.id), ('status', '=', True)])
            if time_stay:
                raise ValidationError("Khách Hàng {0} đã đặt phòng {1}, vui lòng thanh toán hoá rồi đặt lại".format(i.guest_ids.name, i.room_ids.name))
            
    @api.onchange('checkout')
    def _days_stay(self):
        if self.checkout:
            c = self.checkout - self.checkin
            timee = timedelta(hours=12)
            duration = c / timee
            temp = 0;
            if duration > 0:
                if duration < 1:
                    duration += 1
                    temp = int(duration)
                    self.time_stay = temp
                else:
                    temp = int(duration)
                    if duration > temp:
                        duration += 1
                        temp = int(duration)
                        self.time_stay = temp
                    else:
                        temp = int(duration)
                        self.time_stay = temp
            if duration == 0:
                self.time_stay = 0
            
            
