# -*- coding: utf-8 -*-
from odoo import http

# class HrContracts(http.Controller):
#     @http.route('/hr_contracts/hr_contracts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contracts/hr_contracts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contracts.listing', {
#             'root': '/hr_contracts/hr_contracts',
#             'objects': http.request.env['hr_contracts.hr_contracts'].search([]),
#         })

#     @http.route('/hr_contracts/hr_contracts/objects/<model("hr_contracts.hr_contracts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contracts.object', {
#             'object': obj
#         })