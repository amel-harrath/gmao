from odoo import models, fields

class Attribut(models.Model):
    _name = 'attribut'


    intit = fields.Char(string="Intitulé",)
    classe = fields.Integer(string="Classes",)
    desc = fields.Text(string="Description",)
    date = fields.Date(string="Date",)
    date_version = fields.Datetime(string="Date Version",)
    n_version = fields.Integer(string="N° Version",)

    eqpt_attributs_id = fields.Many2one('topographie', 'Topographie', invisible=True,)
    gp_attributs_id = fields.Many2one('groupes', 'Groupe', invisible=True,)
