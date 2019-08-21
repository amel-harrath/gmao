from odoo import models, fields

class Modele_equipe(models.Model):
    _name = 'modele_equipe'


    composition = fields.Integer(string="composition",)
    responsable = fields.Integer(string="responsable",)
    equipes = fields.Many2one('equipe', string="Equipes",)
    jour_semaine = fields.Selection(selection=[('0','0.Lundi'),('1','1.Mardi'),('2','2.Mercredi'),('3','3.Jeudi'),('4','4.Vendredi'),('5','5.Samedi'),], string="Jour Semaine",)
    
   