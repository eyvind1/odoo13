# -*- coding: utf8 -*-

from odoo import models, fields, api

class CreateApp(models.TransientModel):
    _name = "create.app"

    idm = fields.Many2one('colegiotb', "Nombre")
    app_date = fields.Date("App Date")
    


    def print_matricula(self):
        """ vals = []
        sale = self.env['reporte.matricula'].search([('app_date','=',self.app_date)])
        for order in sale:
            vals.append({
                'name':order.name,
                'edad':order.edad
            })

        data = {
            'model':'reporte.matricula',
            'vals': vals,
            'app_date':self.app_date
        } """

        data ={
            "model":"create.app",
            "form": self.read()[0]
        }
        return self.env.ref("colegiomodule.report_matricula").report_action(self, data=data) 