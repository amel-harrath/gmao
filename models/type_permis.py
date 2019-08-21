from odoo import models, fields

class Type_Permis(models.Model):
    _name = 'type_permis'

    code = fields.Char(string="Code",required=True,)
    desc = fields.Text(string="Description",)

    remarques = fields.Text(string="Remarques",)