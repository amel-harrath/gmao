from odoo import models, fields

class Consignes(models.Model):
    _name = 'consignes'
    
    
    code = fields.Char()

    topo_id = fields.Many2one('topographie', 'Equipement', required=True,)
    desc = fields.Text(string="Description", related='topo_id.description',)

    afaire = fields.Many2many('details_consignes','consignes_afaire','consignes_id','details_id', 'A Faire',)
    anepasfaire = fields.Many2many('details_consignes','consignes_anepasfaire','consignes_id','details_id', 'A ne pas Faire',)

