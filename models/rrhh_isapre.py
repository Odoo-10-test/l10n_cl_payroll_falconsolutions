# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class rrhh_isapre(models.Model):
    _description = "Isapre"
    _name = 'rrhh.isapre'
    name = fields.Char('Name', translate=True)
    rut = fields.Char('Rut', translate=True)
    codigo = fields.Integer('Codigo')