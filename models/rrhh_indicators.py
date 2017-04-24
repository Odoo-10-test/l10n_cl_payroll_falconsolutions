# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class rrhh_indicators(models.Model):
    _description = "Indicators"
    _name = 'rrhh.indicators'
    name = fields.Char("Name")

    # UF y UTM
    ind_uf = fields.Float('UF Fin de mes')
    ind_utm = fields.Float('UTM Fin de mes')
    ind_uta = fields.Float('UTA')

    # Asignación Familiar
    ind_asignacion_familiar_t1 = fields.Float('Asignación Familiar Tramo 1')
    ind_asignacion_familiar_t2 = fields.Float('Asignación Familiar Tramo 2')
    ind_asignacion_familiar_t3 = fields.Float('Asignación Familiar Tramo 3')
    ind_asignacion_familiar_t4 = fields.Float('Asignación Familiar Tramo 4')

    ind_asignacion_familiar_ma = fields.Float('Asignación Familiar Monto A')
    ind_asignacion_familiar_mb = fields.Float('Asignación Familiar Monto B')
    ind_asignacion_familiar_mc = fields.Float('Asignación Familiar Monto C')
    ind_asignacion_familiar_md = fields.Float('Asignación Familiar Monto D')

    # Seguro de cesantia
    ind_contrato_plazo_indefinido_empleador = fields.Float('Contrato plazo indefinido empleador')
    ind_contrato_plazo_indefinido_trabajador = fields.Float('Contrato plazo indefinido trabajador')
    ind_contrato_plazo_fijo_empleador = fields.Float('Contrato plazo fijo empleador')
    ind_contrato_plazo_indefinido_empleador_11 = fields.Float('Contrato plazo Indefinido empleador > 11 años')

    # Deposito convenio
    ind_deposito_convenio = fields.Integer('Deposito convenio')

    # Rentas Topes Disponible
    ind_renta_tope_af_afp = fields.Integer('Renta tope afiliado AFP')
    ind_renta_tope_af_ips = fields.Integer('Renta tope afiliado IPS')
    ind_renta_tope_seg_cesantia = fields.Integer('Renta tope seguro cesantia')
    ind_renta_tope_imponible_salud = fields.Integer('Tope Imponible Salud')

    # Rentas Mínima Disponible
    ind_sueldo_minimo = fields.Float('Sueldo mínimo')
    ind_sueldo_minimo_18_65 = fields.Float('Sueldo Mínimo Menores de 18 y mayores de 65')
    ind_sueldo_minimo_casa_particular = fields.Float('Sueldo mínimo trabajadores de casa particular')
    ind_sueldo_minimo_fines_no = fields.Float('Sueldo mínimo para fines no remuneracionales:')

    # TASA COTIZACIÓN OBLIGATORIO AFP
    ind_afp_capital_dependientes = fields.Float('Tasa AFP Capital Dependientes')
    ind_afp_cuprum_dependientes = fields.Float('Tasa AFP Cuprum Dependientes')
    ind_afp_habitat_dependientes = fields.Float('Tasa AFP Habitat Dependientes')
    ind_afp_planvital_dependientes = fields.Float('Tasa AFP PlanVital Dependientes')
    ind_afp_provida_dependientes = fields.Float('Tasa AFP Plovida Dependientes')
    ind_afp_modelo_dependientes = fields.Float('Tasa AFP Modelo Dependientes')

    ind_sis_capital_dependientes = fields.Float('Tasa SIS Capital Dependientes')
    ind_sis_cuprum_dependientes = fields.Float('Tasa SIS Cuprum Dependientes')
    ind_sis_habitat_dependientes = fields.Float('Tasa SIS Habitat Dependientes')
    ind_sis_planvital_dependientes = fields.Float('Tasa SIS PlanVital Dependientes')
    ind_sis_provida_dependientes = fields.Float('Tasa SIS Plovida Dependientes')
    ind_sis_modelo_dependientes = fields.Float('Tasa SIS Modelo Dependientes')

    ind_afp_capital_independientes = fields.Float('Tasa AFP Capital Independientes')
    ind_afp_cuprum_independientes = fields.Float('Tasa AFP Cuprum Independientes')
    ind_afp_habitat_independientes = fields.Float('Tasa AFP Habitat Independientes')
    ind_afp_planvital_independientes = fields.Float('Tasa AFP PlanVital Independientes')
    ind_afp_provida_independientes = fields.Float('Tasa AFP Plovida Independientes')
    ind_afp_modelo_independientes = fields.Float('Tasa AFP Modelo Independientes')

    # Trabajos Pesados
    ind_trab_pesado_total = fields.Float('Trabajo Pesado Total')
    ind_trab_pesado_empleador = fields.Float('Trabajo Pesado Empleador')
    ind_trab_pesado_empleado = fields.Float('Trabajo Pesado Empleado')

    ind_trab_menos_pesado_total = fields.Float('Trabajo Menos Pesado Total')
    ind_trab_menos_pesado_empleador = fields.Float('Trabajo Menos Pesado Empleador')
    ind_trab_menos_pesado_empleado = fields.Float('Trabajo Menos Pesado Empleado')


    # AHORRO PREVISIONAL VOLUNTARIO (APV)
    ind_apv_tope_mensual = fields.Integer('APV tope mensual')
    ind_apv_tope_anual = fields.Integer('APV tope anual')

    # Otros campos ---------------------
    ind_caja_compensacion = fields.Float('Caja de compensacion')
    ind_fonasa = fields.Float('Fonasa')
    ind_mutual = fields.Float('Mutual de Seguridad')

    # Campos de la compañia
    emp_mutual_nombre = fields.Char('Nombre Mutual')
    emp_mutual_valor = fields.Float('Valor Mutual')

    emp_caja_compensacion_nombre = fields.Char('Nombre Caja Compensación')
    emp_caja_valor = fields.Float('Valor Mutual')


    # Link
    @api.multi
    def go_to_link(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.previred.com/web/previred/indicadores-previsionales',
            'target': 'new',
        }

    # Valores que cambiaran si cambia la UF
    @api.onchange('ind_uf')
    def onchange_ind_uf(self):
        self.ind_renta_tope_af_afp = self.ind_uf * 75.7
        self.ind_renta_tope_af_ips = self.ind_uf * 60
        self.ind_renta_tope_seg_cesantia = self.ind_uf * 113.5

        self.ind_apv_tope_mensual = self.ind_uf * 50
        self.ind_apv_tope_anual = self.ind_uf * 600

        self.ind_deposito_convenio = self.ind_uf * 900







