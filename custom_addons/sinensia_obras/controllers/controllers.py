# -*- coding: utf-8 -*-
from odoo import http

# class SinensiaObras(http.Controller):
#     @http.route('/sinensia_obras/sinensia_obras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sinensia_obras/sinensia_obras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sinensia_obras.listing', {
#             'root': '/sinensia_obras/sinensia_obras',
#             'objects': http.request.env['sinensia_obras.sinensia_obras'].search([]),
#         })

#     @http.route('/sinensia_obras/sinensia_obras/objects/<model("sinensia_obras.sinensia_obras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sinensia_obras.object', {
#             'object': obj
#         })