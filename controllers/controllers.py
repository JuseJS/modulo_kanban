#-*- coding: utf-8 -*-
from odoo import http


class ListaTareas2(http.Controller):
    @http.route('/lista_tareas2/lista_tareas2', auth='public')
    def index(self, **kw):
        return "Hello, world , lista_tareas2"

    @http.route('/lista_tareas2/lista_tareas2/objects', auth='public')
    def list(self, **kw):
        return http.request.render('lista_tareas2.listing', {
            'root': '/lista_tareas2/lista_tareas2',
            'objects': http.request.env['lista_tareas2.lista_tareas2'].search([]),
        })

    @http.route('/lista_tareas2/lista_tareas2/objects/<model("lista_tareas2.lista_tareas2"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('lista_tareas2.object', {
            'object': obj
        })

