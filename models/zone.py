from odoo import models, fields

class Zone(models.Model):
    _name = 'zone'

    code = fields.Char(string="Code",)
    descp = fields.Text(string="Description",)
    entite = fields.Char(string="Entité",)
    resp = fields.Char(string="Responsable",)
    cout = fields.One2many('cout','zone_cout_id','Cout')
   
