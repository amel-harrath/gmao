from odoo import models, fields

class Permis_Travail(models.Model):
    _name = 'permis_travail'

    code=fields.Char(string="Code",)
    desc = fields.Text(string="Description",)
    type_permis = fields.Char(string="Type Permis",)