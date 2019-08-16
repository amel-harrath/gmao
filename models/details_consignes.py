from odoo import models, fields

class Details_Consignes(models.Model):
    _name = 'details_consignes'

    code = fields.Char(string="Codification",)
    desc = fields.Text(string="Description",) 