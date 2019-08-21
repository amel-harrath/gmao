from odoo import models, fields

class Famille(models.Model):
    _name = 'famille'

    code = fields.Char(string="Famille",required=True,)
    desc = fields.Text(string="Description",)

