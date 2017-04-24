# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class rrhh_ccaf(models.Model):
    _description = "CCAF"
    _name = 'rrhh.ccaf'
    name = fields.Char('Glosa')
    codigo = fields.Integer('Codigo')