# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class rrhh_mutual(models.Model):
    _description = "Mutual"
    _name = 'rrhh.mutual'
    name = fields.Char('Glosa')
    codigo = fields.Integer('Codigo')