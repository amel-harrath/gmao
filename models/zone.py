from odoo import models, fields

class Zone(models.Model):
    _name = 'zone'

    code = fields.Char(string="Code",)
    descp = fields.Text(string="Description",)
    entite = fields.Char(string="Entité",)
    resp = fields.Char(string="Responsable",)