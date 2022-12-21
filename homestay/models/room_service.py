from odoo import models, fields, api
from PIL.ImageChops import offset


class Room_Service(models.Model):
    _name = 'aaroom.service'
    
    name = fields.Char(string="ten room service de test", default="Test Choi choi")
    price_service = fields.Float(string="Giá dịch vụ", group_operator='max',compute='_compute_name')
    room_id = fields.Many2one("aaroom", string="Số phòng", ondelete='restrict')
    service_id = fields.Many2one("aaservice", string="Tên dịch vụ", ondelete='restrict')
    invoice_ids = fields.Many2one("aainvoice", string="thuc su k can dung den", ondelete='restrict')

    @api.depends('service_id')
    def _compute_name(self):
        for i in self:
            if i.service_id: 
                i.price_service = i.service_id.price
            else: 
                i.price_service = 0
    
    def price_servicee(self):
        a = ['name', 'service_id.name']
        return a
    
    def btn_mapped(self):
        c = self.env["aaroom.service"].price_servicee()
        for d in c:
            a = self.env["aaroom.service"].search([]).mapped(d)
            print(a, " btn_mapped ", d)
        return a
    
    def btn_create(self):
        a = self.env["aaroom.service"].create([{'name': 'Phong doi', 'service_id':1}, {'name': 'Phong doi 2', 'service_id':1}])
        print(a, "btn_create")
        return a
    
    def btn_write(self):
        a = self.env["aaroom.service"].search([('price_service', '>', 0)]).write({'name': 'test ham write', 'service_id': [(0, 0,
                                                  {'name': "test ham write", 'price': 180000}
                                                    )]})
        print(a, "btn_write")
        return a
    
    def btn_browse(self):
        a = self.env["aaroom.service"].browse(self.id).price_service
        a += 3456
        print(a, "btn_browse")  
        return a
    
    def btn_search(self):
        a = self.env["aaroom.service"].search([('price_service', '>', 0)], offset=1, limit=8, order='room_id desc')
        print(a, "btn_search")
        return a
    
    def btn_search_count(self):
        a = self.env["aroom.service"].search_count([('price_service', '>', 0)])
        print(a, "btn_search_count")
        return a
    
    def btn_name_create(self):
        a = self.env['aaroom.service'].name_create('ten create')
        # b = self.env["aaroom.service"].search([]).service_id
        print(a, "btn_name_create")
        return a
    
    def btn_default_get(self):
        a = self.env['aaroom.service'].default_get(['name'])
        print(a, "btn_default_get")
        return a
    
    def btn_name_search(self):
        a = self.env["aaroom.service"].name_search('Phòng 101', [])
        print(a, "btn_name_search")
        return a
    
    def btn_search_count(self):
        a = self.env["aaroom.service"].search_count([('price_service', '<=', 0)])
        print(a, "btn_search_count")
        return a
    
    def btn_read(self):
        a = self.price_service.search([('price_service', '>', 0)])
        print(a, "btn_read")
        return a
    
    def btn_fields_get(self):
        a = self.env["aaroom.service"].fields_get(['name', 'name'])
        print(a, "btn_fields_get")
        return a
    
    def btn_read_group(self):
        a = self.env["aaroom.service"].read_group([], ['name'], ['price_service'])
        print(a, "btn_read_group")
        return a
    
    def btn_copy(self):
        a = self.env["aaroom.service"].search(['id', '=', self.id]).copy()
        print(a, "aaaaaa")
        return a
    
    def btn_filtered(self):
        a = self.env["aaroom.service"].search([]).filtered('service_id.name')
        # b = self.env["aaroom.service"].search([]).service_id.name
        c = self.name = 'name'
        print(c)
        print(a, "aaaaaa")
        return c
    
    @api.model
    def create(self, val):
        if val.get('name'):
            val['name'] = val['name'].upper()
        return super(Room_Service, self).create(val)

# nếu k ghi model
    def write(self, vals):
        if vals.get('name'):
            vals["name"] = vals["name"].upper()
        return super(Room_Service, self).write(vals)
    
