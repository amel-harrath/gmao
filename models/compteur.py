from odoo import models, fields

class Compteur(models.Model):
    _name = 'compteur'

    compteur = fields.Char(string="Compteur",)
    desc = fields.Text(string="Description",)
    type_compteur = fields.Char(string="Type Compteur",)
    typee = fields.Char(string="Type",)
    unite = fields.Char(string="Unité",)
    freq = fields.Integer(string="Fréquence",)

