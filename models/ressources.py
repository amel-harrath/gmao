from odoo import models, fields

class Ressources(models.Model):
    _name = 'ressources'

    code = fields.Char(string="Ressources",required=True,)
    desc = fields.Text(string="Description",)
    

    intervention_id = fields.Many2one('intervention',' Intervention', invisible=True,)