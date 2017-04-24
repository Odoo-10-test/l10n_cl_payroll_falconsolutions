# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class hr_payslip(models.Model):

    _inherit = 'hr.payslip'
    ind_id = fields.Many2one('rrhh.indicators', 'Indicadores Previred')