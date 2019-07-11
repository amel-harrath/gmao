from odoo import models, fields

class Eqpt_Intervention(models.Model):
    _name = 'eqpt_intervention'

    intervention = fields.Char(string="intervention",)
    eqpt_type = fields.Char(string="Type",)
    eqpt_class = fields.Char(string="Class",)
    c_charge = fields.Char(string="C Charge",)
    #type_permis = fields.Char()
    #superviseur = fields.Char()
    #code_priorite = fields.Char()
    #dern_MAJ = fields.Date()
    #planification = fields.Char()
    #duree = fields.Integer()
    #priorite = fields.Integer()