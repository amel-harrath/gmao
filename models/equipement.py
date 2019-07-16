from odoo import models, fields

class Equipement(models.Model):
    _name = 'equipement'

    code = fields.Char(string="Equipement",)
    desc = fields.Text(string="Description",)
    niv = fields.Integer(string="Niveau",)
    zone = fields.Many2one('zone',string="Zone",)
    famille = fields.Char(string="Famille")
    c_charge = fields.Char(string="C Charge",)
    fonc = fields.Many2one('fonction', string="Fonction",)
    type_permis = fields.Char(string="Type Permis",)
    parent_geo = fields.Char(string="Parent Géograph.",)
    n_eqpt = fields.Integer(string="N° Equipement",)
    pt_ot_correctif = fields.Boolean(string="PT pour OT Correctf",)
    entite = fields.Char(string="Entité",)
    cat = fields.Selection(selection=[('0','0.Technique'),('1','1.Géographique'),], string=" ",)
    etat_eqpt = fields.Char(string="Etat Equipement",)
    eqpt_arret = fields.Boolean(string="Equipement Arrêt",)