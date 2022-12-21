from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Room(models.Model):
    _name = 'aaroom'
    # _parent_store = True
    # _parent_name = 'parent_id'
    _description = 'The bedroom of the house'
    # _sql_constraints = [('name_exists', 'UNIQUE(name)', "Room name was exists")]
    
    name = fields.Char(string="Số phòng", help='This field is entered with string', copy=False)
    floor = fields.Integer(string='Tầng')
    status = fields.Boolean(string='Đang sử dụng', default=False, compute='_dayss_stay', store=True)
    image = fields.Binary(string='Ảnh')
    state = fields.Selection(string='Trạng Thái', selection=[('blank', 'Phòng Trống'),
                                                        ('over', 'Phòng Đã D')],
                                                    default='new')  
    price = fields.Float(string='Giá phòng', digits=('Somethings'))
    amount = fields.Integer(string='Số lượng người')
    booking = fields.One2many("aabooking", "room_ids")
    # home_id = fields.Many2one(comodel_name="aahome", string="Homestay trực thuộc", ondelete='restrict', required=True)
    # parent_id = fields.Many2one(comodel_name='aaroom', index=True, ondelete='cascade')
    # parent_path = fields.Char(index=True, readonly=True) 
    
    @api.onchange('floor')
    def _onchange_ethnicity_id(self):
            if self.name:
                self.name = 'Phòng ' + str(self.floor)+ '0'+ self.name
    
    # @api.depends('booking.room_ids')
    # def _dayss_stay(self):
    #     for i in self:
    #         if i.booking.room_ids:
    #             if i.status == False:
    #                 i.status = True
    #             else:
    #                 raise ValidationError("Phong {0} đã duoc dat".format(i.name))
    
    # @api.constrains('name')
    # def _constrains(self):
    #     for i in self:
    #         test = self.env['aaroom'].search([('name', '=', i.name), ('home_id','!=', i.home_id)])
    #         if test:
    #             raise ValidationError("Tên {0} đã tồn tại".format(i.name))
