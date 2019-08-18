from odoo import models, fields

class Allocation_Employe_Ot(models.Model):
    _name = 'allocation_employeot'


    employe = fields.Many2one('employe', string="Employé", required=True,)
    desc = fields.Char(string="Description", related="employe.nom",)
    date_alloc = fields.Date('Date Allocation', required=False, readonly=True, select=True
                                , default=lambda self: fields.datetime.now().date())
    Hrs_planifiees = fields.Integer(string="Hrs Planifiées",)
    allocation = fields.Selection(selection=[('0','Non Réalisé'),('1','Réalisé'),], string="Allocation",)
    qualif = fields.Selection(selection=[('0','Approuvé'),('1','Rejeté'),('2','Annulé')], string='Qualification',)

    details_ot_ids = fields.Many2one('details_ot', 'Details OT', invisible=True,)