# -*- coding: utf8 -*-

from odoo import models,fields,api

class Colegio(models.Model):
    _name = "colegiotb"

    name = fields.Char("Nombre",required=True)
    edad = fields.Integer("Edad")
    cellphone = fields.Integer("Celular")
    email = fields.Char("Email",required=True)
    image = fields.Binary("Image")
    status = fields.Selection(selection=[("alumno","Alumno"),("profesor","Profesor"),("director","Director")])

class Reporte_matricula(models.Model):
    _name = "reporte.matricula"

    name = fields.Char("Nombre",required=True)
    edad = fields.Integer("Edad")
    cellphone = fields.Integer("Celular")
    email = fields.Char("Email",required=True)