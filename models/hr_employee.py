# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime


class HrEmploye(models.Model):

    _description = "Hr Employe"
    _inherit = 'hr.employee'

    def rh_full_name(self):
        self.rh_full_name = self.name + ' ' + self.rh_middle_name

    def get_total_carga(self):
        self.total_carga = round(sum(line.list_monto for line in self.rh_cargas_ids))

    ###### FIELDS ######

    rh_rut = fields.Char(
        "RUN", size=100, help='Rol Único Nacional')

    rh_middle_name = fields.Char("Segundo Nombre", size=100)

    rh_full_name = fields.Char("Full Name", size=200, help='Nombre Completo',compute='rh_full_name')

    rh_last_name = fields.Char(
        "Primer Apellido", size=100, help='Last employee name')

    rh_slast_name = fields.Char(
        "Segundo Apellido", size=100, help='Mother last name')

    rh_emergency = fields.Char("Contacto Emergencia", size=100, help='Contacto emergencia')

    rh_emergency_phone = fields.Char("Teléfono Emergencia", size=100, help='Teléfono emergencia')

    rh_cargas_ids = fields.One2many('l.cargas', 'employee_id', string='Cargas')

    rh_asignaciones_ids = fields.One2many('l.asignaciones', 'employee_id', string='Asignaciones')

    rh_descuentos_ids = fields.One2many('l.descuentos', 'employee_id', string='Descuentos')


    total_carga = fields.Float("Total", compute='get_total_carga')

    @api.multi
    @api.onchange('rh_rut')
    def _comprueba_rut(self):
        if self.rh_rut:
            int_rut = self.rh_rut
            int_rut = int_rut.replace("-", '')
            int_rut = int_rut.replace(".", '')

            rut = int_rut[:-1]
            dig = int_rut[-1]



            resto = ""
            ok = False

            if len(int_rut) > 8:

                n1 = rut[0]
                m1 = int(n1)*3

                n2 = rut[1]
                m2 = int(n2)*2

                n3 = rut[2]
                m3 = int(n3)*7

                n4 = rut[3]
                m4 = int(n4)*6

                n5 = rut[4]
                m5 = int(n5)*5

                n6 = rut[5]
                m6 = int(n6)*4

                n7 = rut[6]
                m7 = int(n7)*3

                n8 = rut[7]
                m8 = int(n8)*2

                suma = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
                resto = suma / 11
                resto = 11 - ( suma - resto * 11 )

                if resto == 10 or resto == 11:
                    resto = 'K'
                    ok = True

                if dig == str(resto):
                    ok = True

            else:
                ok = True

            # Formateamos el RUT con el estandar 24.063.888-6
            position = len(int_rut) - 1
            int_rut =  int_rut[:position] + '-' + int_rut[position:]
            int_rut =  int_rut[:-5] + '.' + int_rut[-5:]
            if len(int_rut) > 9:
                int_rut =  int_rut[:-9] + '.' + int_rut[-9:]

            if not ok:
                self.rh_rut = ''
            else:
                self.rh_rut = int_rut


    ###### PREVISION Y SALUD ######

    rh_type_worker = fields.Selection(
            [('0','Activo (no pensionado)'),
             ('1','Pensionado y cotiza'),
             ('2 ','Pensionado y no cotiza '),
             ('3','Activo > 65 años (nunca pensionado)')],
             'Tipo trabajador', size=1 ,default='0')

    rh_type_prevision = fields.Selection(
            [('SIP','Sin Institución Previsional'),
             ('AFP','AFP'),
             ('INP ','IPS(ex INP)')],
            'Previsión', size=1 ,default='SIP')

    rh_afp_id = fields.Many2one('rrhh.afp', 'AFP')

    rh_aporte_voluntario = fields.Integer(
        'APV en AFP', help="Monto en pesos que el trabajador ahorra voluntariamente en la AFP")

    isapre_id = fields.Many2one('rrhh.isapre', 'Institución salud', help="¿Isapre o Fonasa?")
    rh_isapre_pactado = fields.Integer(
        'Monto Salud', help="Sólo si es Isapre, indicar la cotización pactada")

    rh_type_isapre_moneda = fields.Selection(
            [('1','Pesos'),
             ('2','UF')],
            'Salud Moneda', size=1 ,default='1', help="Sólo si es Isapre, ¿cuál es la moneda de la cotización pactada con la Isapre?")


class List_Cargas(models.Model):
    _name = 'l.cargas'
    list_run = fields.Char("RUN", size=12)
    list_name = fields.Char("Nombre", size=25)
    list_nacimiento = fields.Date('Fecha de Nacimiento')
    list_edad_limite = fields.Integer("Edad Limite")
    list_tipo = fields.Selection(
            [('1','Simple'),
            ('2','Maternal'),
            ('3','Inválida')],
            'Tipo', size=1 ,default='1')
    list_obs = fields.Char("Observación", size=25)
    employee_id = fields.Many2one('hr.employee', "Empleado")



class List_Asignaciones(models.Model):
    _name = 'l.asignaciones'
    list_code = fields.Char("Código", size=5)
    list_glosa = fields.Char("Glosa", size=25)
    list_monto = fields.Integer("Monto")
    rh_type_isapre_moneda = fields.Selection(
            [('1','Pesos'),
            ('2','UF'),
            ('3','Dolar'),
            ('4','Euros')],
            'Moneda', size=1 ,default='1')
    list_imponible = fields.Boolean("Imponible")
    desde_date = fields.Date('Desde', default = lambda self: datetime.today())
    hasta_date = fields.Date('Hasta')
    list_obs = fields.Char("Observación", size=25)
    employee_id = fields.Many2one('hr.employee', "Empleado")


class List_Descuentos(models.Model):
    _name = 'l.descuentos'
    list_code = fields.Char("Código", size=5)
    list_glosa = fields.Char("Glosa", size=25)
    list_monto = fields.Integer("Monto")
    rh_type_isapre_moneda = fields.Selection(
            [('1','Pesos'),
            ('2','UF'),
            ('3','Dolar'),
            ('4','Euros')],
            'Moneda', size=1 ,default='1')
    list_imponible = fields.Boolean("Imponible")
    desde_date = fields.Date('Desde', default = lambda self: datetime.today())
    hasta_date = fields.Date('Hasta')
    list_obs = fields.Char("Observación", size=25)
    employee_id = fields.Many2one('hr.employee', "Empleado")
