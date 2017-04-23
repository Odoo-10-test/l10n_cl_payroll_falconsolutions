# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HrRuler(models.Model):

    _description = "Hr Ruler"
    _inherit = 'hr.salary.rule'

    ###### FIELDS ######

    start_date = fields.Date("Start Date", help='Start Date')
    end_date = fields.Date("End Date", help='Start Date')









