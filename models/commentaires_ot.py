from odoo import models, fields, api

class Commentaires_Ot(models.Model):
    _name = 'commentaires_ot'


    desc = fields.Text(string="",)
    date = fields.Datetime('Date', required=False, readonly=True, select=True
                                , default=lambda self: fields.datetime.now())
    details_ot_ids = fields.Many2one('details_ot', 'Details OT', invisible=True,)
