from odoo import models, fields

class Details_dessins(models.Model):
    _name = 'details_dessins'

    num = fields.Integer(string="N°",required=True,)
    date_creation = fields.Datetime("Créé le", required=False, readonly=True
                                , default=lambda self: fields.datetime.now())
    version = fields.Float(string="Version",)
    empl = fields.Char(string="Emplacement",) 


    manuels_dessins_ids = fields.Many2one('manuels_dessins', 'ManuelsEtDessins',)
