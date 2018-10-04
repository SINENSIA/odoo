# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SocialSecurity(models.Model):
    _name = 'hr_contract.social_security'

    x_ss_scheme = fields.Selection([('GENERAL_SCHEME', 'General Scheme'), ('OTHERS', 'Others')])

# class hr_contracts(models.Model):
#     _name = 'hr_contracts.hr_contracts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
