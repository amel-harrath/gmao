from odoo import models, fields

class Defauts(models.Model):
    _name = 'defauts'
    
    
    topo_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='topo_id.description',)


    date = fields.Datetime(string='Date',)
    type_def = fields.Selection(selection=[('0','Fich. Base'),('1','Famille'),], string='',)
    symptome = fields.Char(string='Symptôme',)
    defaut = fields.Char(string='Défaut',)
    cause = fields.Char(string='Cause',)
    remede = fields.Char(string='Remède',)
    duree = fields.Integer(string='Durée',)
    num_ot = fields.Integer(string='N° OT',)
    valeur_cpt = fields.Integer(string='Valeur Compteur',)
    cout_ot = fields.Float(string='Coût OT',)
   
