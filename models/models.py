# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas2(models.Model):
    _name = 'lista_tareas2.lista_tareas2'
    _description = 'lista_tareas2.lista_tareas2'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    fecha_asignada = fields.Datetime(string="Fecha Asignada")

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad < 10:
                record.urgente = True
            else:
                record.urgente = False

