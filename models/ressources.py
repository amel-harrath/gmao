from odoo import models, fields

class Ressources(models.Model):
    _name = 'ressources'

    code = fields.Char(string="Ressources",)
    desc = fields.Text(string="Description",)
    