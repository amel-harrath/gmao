from odoo import models, fields

class Mouvement(models.Model):
    _name = 'mouvement'

    
    type_mouvement = fields.Selection(selection=[('0','0.Tous'),('1','1.Normal'),('2','2.Géo.Technique'),('3','3.CC/Entité'),], string="Type",)
    date = fields.Datetime('Date', required=False, readonly=False
                                , default=lambda self: fields.datetime.now())
    niv = fields.Integer(string="Niveau",)
    zone = fields.Many2one('zone', string='Zone',)
    parent = fields.Char(string="Parent",)
    fonc = fields.Many2one('fonction', string="Fonction",)
    desc = fields.Char(string="Description",)

    equipement_id = fields.Many2one('topographie', 'Topographie', invisible=True,)