from odoo import models, fields

class Groupe(models.Model):
    _name = 'groupe'

    code = fields.Char(string="Equipement")
    desc = fields.Text(string="Description",)
    zone = fields.Many2one('zone',string="Zone",)
    famille = fields.Char(string="Famille")
    c_charge = fields.Char(string="C Charge",)
    fonc = fields.Many2one('fonction', string="Fonction",)
    entite = fields.Char(string="Entité")
