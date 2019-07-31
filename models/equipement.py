from odoo import models, fields

class Equipement(models.Model):
    _name = 'equipement'

    code = fields.Char(string="Equipement",)
    desc = fields.Text(string="Description",)
    niv = fields.Integer(string="Niveau",)
    zone = fields.Many2one('zone',string="Zone",)
    famille = fields.Char(string="Famille")
    c_charge = fields.Char(string="C Charge",)
    fonc = fields.Char(string="Fonction",)
    parent_geo = fields.Char(string="Parent Géograph.",)
    entite = fields.Char(string="Entité",)
    etat_eqpt = fields.Char(string="Etat Equipement",)