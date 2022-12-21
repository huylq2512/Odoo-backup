from odoo import fields, models,api


class basic(models.Model):
    _name = 'aatest'
    
    employee_id = fields.Integer(string='id', default=None)
    employee_name = fields.Char(string='name')
    float2t = fields.Float(string='aca', digits=(2,10))
    testround = fields.Integer()
    employeee = fields.Char(string='a')
    upper = fields.Char(compute='_compute_upper', readonly=False)
    

   
    def _compute_upper(self):
        for rec in self:
            rec.upper = rec.upper.upper() if rec.upper else False
           
        # new_students = self.env['aatest'].create([{'float2t': 321.2323222}])

 
