from odoo import models,fields,api

class Colegio(models.Model):
    _name = "colegiotb"

    name = fields.Char("Nombre")
    edad = fields.Integer("Edad")
    cellphone = fields.Integer("Celular")
    status = fields.Selection(selection=[("alumno","Alumno"),("profesor","Profesor"),("director","Director")])