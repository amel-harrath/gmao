from odoo import models, fields

class Entite(models.Model):
    _name = 'entite'


    code = fields.Integer(string="Code", required=True,)
    desc = fields.Char(string="Description",)