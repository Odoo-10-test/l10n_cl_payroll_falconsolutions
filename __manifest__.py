# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Payroll Chile MFH',
    'version': '10.0.0.1.0',
    'author': "Falcón Solutions, Marlon Falcón",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Settings',
    'summary': 'Localización de Recursos Humanos Chile RR.HH',
    'depends': ['hr_payroll'],
    'description': """
Recursos Humanos Chile con Previred
=====================================================
* Agregado campos para trabajar con la nómina Chilena
* Plantilla de datos de Previred
* Genera Archivo de Previred
        """,
    'data': [

        'views/hr_employee_view.xml',
        'views/hr_salary_rule_view.xml',

        'views/rrhh_view.xml',
        'views/rrhh_isapre_view.xml',
        'views/rrhh_indicators_view.xml',
        'views/hr_payslip_view.xml',
        'views/rrhh_afp_view.xml',
        'views/hr_contract_view.xml',

        'data/rrhh_isapre_data.xml',
        'data/rrhh_afp_data.xml',
        'data/hr_salary_rule_category_data.xml',
        'data/hr_contract_type_data.xml',
        'data/hr_contribution_register_data.xml',
        'data/rrhh_indicators_data.xml',
        'data/hr_calendar_data.xml',
        'data/hr_calendar_data.xml',

    ],
    'installable': True,
    'auto_install': False,
    'demo': [
         'demo/hr_employee_data.xml',
         'demo/hr_contract_data.xml',
    ],
    'test': [],
}

