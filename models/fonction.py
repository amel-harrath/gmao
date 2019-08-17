from odoo import models, fields

class Fonction(models.Model):
    _name = 'fonction'

    code = fields.Char(string="Code",)
    descp = fields.Text(string="Description",)
    entite = fields.Many2one('entite', string="Entité",)
    resp = fields.Char(string="Responsable",)
    cout = fields.One2many('cout','fonction_cout_id','Cout')