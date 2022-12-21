from odoo import models, fields, api


class home(models.Model):
    _name = 'aahome'
    _description = 'Place includes rooms and services'

    name = fields.Char(string='Tên Homestay')#,groups='homestay.group_homestay_manager'
    address = fields.Char(string='Địa chỉ')
    room_id = fields.One2many("aaroom", "home_id", string="Phòng trực thuộc")
    
    
# class homeExtend(models.Model):
#     lst = ['ahome']
#     _inherit = lst
#
#     name = fields.Char(string='Homestay', required=True)
#
