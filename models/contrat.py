from odoo import models, fields

class Contrat(models.Model):
    _name = 'contrat'

    code = fields.Char()

    equipement_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='equipement_id.description',)

    details_contrat = fields.One2many('details_contrats','contrat_eqpts_id', 'pieces')
