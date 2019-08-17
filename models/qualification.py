from odoo import models, fields

class Qualification(models.Model):
    _name = 'qualification'


    qualif = fields.Char(string="Qualification", required=True,)
    desc = fields.Char(string="",)
    parent = fields.Char(string="Parent",)
    entite = fields.Many2one('entite', string="Entité",)