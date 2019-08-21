from odoo import models, fields

class Reparable(models.Model):
    _name = 'reparable'

    num_serie = fields.Char(string="N° Série",required=True,)
    article = fields.Char(string="Article",)
    date_remplacement = fields.Datetime(string="Date Remplacement",)
    val_cpt_entrant = fields.Integer(string="Valeur Compteur Entrant",)
    val_cpt_sortant = fields.Integer(string="Valeur Compteur Sortant",)

    eqpt_reparable_id = fields.Many2one('topographie', 'Topographie', invisible=True,)