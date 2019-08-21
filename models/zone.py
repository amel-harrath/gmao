from odoo import models, fields

class Zone(models.Model):
    _name = 'zone'

    code = fields.Char(string="Code",required=True,)
    descp = fields.Text(string="Description",)
    entite = fields.Many2one('entite' ,string="Entité",)
    resp = fields.Char(string="Responsable",)
    cout = fields.One2many('cout','zone_cout_id','Cout')
   
