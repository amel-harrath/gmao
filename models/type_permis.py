from odoo import models, fields

class Type_Permis(models.Model):
    _name = 'type_permis'

    code = fields.Char(string="Code",)
    desc = fields.Text(string="Description",)

    remarques = fields.Text(string="Remarques",)