from odoo import models, fields

class Allocation_Ressources_Ot(models.Model):
    _name = 'allocation_ressourcesot'

    res = fields.Many2one('ressources', string='Ressources', required=True,)
    des = fields.Text(string="Description", related="res.desc",)
    hrs_planifiees = fields.Integer(string="Hrs Planifiées",)
    nb_requis = fields.Integer(string="Nb Requis",)
    jr_deb = fields.Integer(string="Jour Début",)


    details_ot_ids = fields.Many2one('details_ot', 'Details OT', invisible=True,)
