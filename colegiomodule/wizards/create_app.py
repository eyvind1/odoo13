# -*- coding: utf8 -*-

from odoo import models, fields, api

class CreateApp(models.TransientModel):
    _name = "create.app"

    app_date = fields.Date("App Date")