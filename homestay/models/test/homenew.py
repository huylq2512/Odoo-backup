from odoo import models, fields,api
from odoo.exceptions import ValidationError

class homenew(models.Model):
    _name = 'ahomenew'
    
    
    name = fields.Char(string='Name')
    intc = fields.Integer(string="test int")#, compute='_compute_name'
    inta = fields.Integer(string="done")
    namenew = fields.Char(string='Nameeqw')
    dob = fields.Date(string="dob")
    dobb = fields.Date(string="dobb")
    nameneww = fields.Char(string='Nameeqw')
    
    
    def _compute_name(self):
        for i in self:
            if i.inta < 5:
                i.intc = 2
            else:
                i.intc = 7 * 1
    
    @api.onchange('name')
    def _onchange_ethnicity_id(self):
        if self.name:   
            self.namenew = self.name
            
    # @api.constrains('name')
    # def _constrains(self):
    #     for i in self:
    #         test = self.env['ahomenew'].search([('name', '=', i.name), ('id','!=', i.id)])
    #         if test:
    #             raise ValidationError("Tên {0} đã tồn tại".format(i.name))
                       
