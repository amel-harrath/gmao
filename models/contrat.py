from odoo import models, fields

class Contrat(models.Model):
    _name = 'contrat'

    code = fields.Char()

    equipement_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='equipement_id.description',)

    details_contrat = fields.Many2many('details_contrats','contrat_eqpts', 'contrat_eqpt_id','details_contrat_id','Détails Contrats')

