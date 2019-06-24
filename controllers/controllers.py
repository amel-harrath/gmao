# -*- coding: utf-8 -*-
from odoo import http

# class Gmao(http.Controller):
#     @http.route('/gmao/gmao/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gmao/gmao/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gmao.listing', {
#             'root': '/gmao/gmao',
#             'objects': http.request.env['gmao.gmao'].search([]),
#         })

#     @http.route('/gmao/gmao/objects/<model("gmao.gmao"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gmao.object', {
#             'object': obj
#         })