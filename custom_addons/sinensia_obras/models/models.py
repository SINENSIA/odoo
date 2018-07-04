# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sinensia_obras(models.Model):
    _name = 'sinensia_obras.sinensia_obras'
    # inherit='project.task'
    name = fields.Char(string='Civil work name')
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

 #    @api.depends('value')
 #    def _value_pc(self):
 #        self.value2 = float(self.value) / 100