from odoo import models, fields

class Eqpt_Intervention(models.Model):
    _name = 'eqpt_intervention'


    topo_id = fields.Many2one('topographie','Equipement',)
    desc_topo = fields.Text(string=" ", related="topo_id.description",)

    intervention_id = fields.Many2one('intervention', 'Intervention',)
    desc_intr = fields.Text(string=" ", related="intervention_id.description",)
    type_intr = fields.Char(string="Type", related="intervention_id.intr_type",)
    planification = fields.Selection(string="Planification", related="intervention_id.planification",)

    class_intr = fields.Char(string="Classe",)
    c_charge = fields.Char(string="C. Charge",)
    type_permis = fields.Many2one('type_permis','Type Permis',)
    superviseur = fields.Char()
    code_priorite = fields.Char()
    duree = fields.Integer()
    cal_duree = fields.Selection(selection=[('0','0.Jours'),('1','1.Semaines'),('2','2.Mois'),], string=" ",)
    priorite = fields.Integer(string="Priorité",)
