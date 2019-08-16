from odoo import models, fields

class Manuels_Dessins(models.Model):
    _name = 'manuels_dessins'
    
    
    code = fields.Char()

    topo_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='topo_id.description',)

    manuels = fields.One2many('details_dessins','manuels_dessins_ids', 'Manuels',)


