# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class hr_contract(models.Model):

    _description = "Hr Contract"
    _inherit = 'hr.contract'

    ###### FIELDS ######
    sueldo_moneda = fields.Selection(
            [('1','Pesos'),
            ('2','UF'),
            ('3','Dolar'),
            ('4','Euros')],
            'Moneda', size=1 ,default='1')





