from odoo import models, fields

class Pieces_Outils(models.Model):
    _name = 'pieces_outils'

    code = fields.Char()

    equipement_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='equipement_id.description',)

    piece = fields.One2many('details_pieces','pieces_outils_id', 'pieces')

