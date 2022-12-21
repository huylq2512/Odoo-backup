# -*- coding: utf-8 -*-
# from odoo import http


# class Homestay(http.Controller):
#     @http.route('/homestay/homestay/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/homestay/homestay/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('homestay.listing', {
#             'root': '/homestay/homestay',
#             'objects': http.request.env['homestay.homestay'].search([]),
#         })

#     @http.route('/homestay/homestay/objects/<model("homestay.homestay"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('homestay.object', {
#             'object': obj
#         })
