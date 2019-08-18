from odoo import models, fields

class Compteur(models.Model):
    _name = 'compteur'

    compteur = fields.Char(string="Compteur",)
    desc = fields.Text(string="Description",)
    type_compteur = fields.Char(string="Type Compteur",)
    typee = fields.Char(string="Type",)
    unite = fields.Char(string="Unité",)
    freq = fields.Integer(string="Fréquence",)
    date_releve = fields.Date(string="Date Relevé",)
    val_max_jr = fields.Integer(string="Valeur Max journalière",)
    valeur = fields.Integer(string="Valeur",)

    ot_id = fields.Many2one('details_ot', invisible=True,)
