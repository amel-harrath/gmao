from odoo import models, fields

class Details_Pieces(models.Model):
    _name = 'details_pieces'



    article = fields.Char(string="Article",)
    info = fields.Text(string="Info",)
    origine = fields.Integer(string="Origine",)
    groupe = fields.Char(string="Groupe",)
    qte_min = fields.Integer(string="Qté Mini",) 
    qte_utilise = fields.Integer(string="Qte Utilisée",)
    unite = fields.Char(string="Unité",) 


    pieces_outils_id = fields.Many2one('pieces_outils', 'Pieces')


