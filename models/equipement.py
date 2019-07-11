from odoo import models, fields

class Equipement(models.Model):
	_name = 'equipement'

    equipement = fields.Char()
    description = fields.Text()
