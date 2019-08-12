from odoo import models, fields

class Details_Pieces(models.Model):
    _name = 'details_pieces'



    article = fields.Char(string="Article",)
    info = fields.Text(string="Info",)
    origine = fields.Text(string="Origine",)
    groupe = fields.Char(string="Groupe",)
    qte_min = fields.Char(string="Qté Mini",) 