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
    parent_geo = fields.Char(string="Parent Géograph.",)
    entite = fields.Many2one('entite', string="Entité",)
    etat_eqpt = fields.Selection(string="Etat Système",
     selection=[('0','0.Normal'),
     ('1','1.Dégradé'),
     ('2','2.Préparation'),
     ('3','3.Rebus'),
     ('4','4.Consigé'),],)
    type_eqpt = fields.Selection(selection=[('0','0.Technique'),('1','1.Géographique'),], string="Type",)
