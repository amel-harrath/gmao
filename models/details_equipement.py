from odoo import models, fields

class Equipement(models.Model):
    _name = 'details_equipement'


    code = fields.Many2one('equipement', string="Code",)
    description = fields.Text(string="Description",)
    etat_sys = fields.Selection(string="Etat Système",
     selection=[('0','0.Normal'),
     ('1','1.Dégradé'),
     ('2','2.Préparation'),
     ('3','3.Rebus'),
     ('4','4.Consigé'),],)
    entite = fields.Char(string="Entité",)
    eqpt_arret = fields.Boolean(string="Equipement Arrêt",)