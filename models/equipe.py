from odoo import models, fields

class Equipe(models.Model):
    _name = 'equipe'


    mat = fields.Char(string="Equipe", required=True,)
    entite = fields.Many2one('entite', string="Entite",)
    type_equipe = fields.Selection(selection=[('0','0.Equipe du matin'),('1','1.Equipe d\'apres midi'),], string="Description",)
    hr_debut = fields.Float('Hr Debut ',)
    hr_fin = fields.Float('Hr Fin ',)
   