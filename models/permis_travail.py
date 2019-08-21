from odoo import models, fields

class Permis_Travail(models.Model):
    _name = 'permis_travail'

    code=fields.Char(string="Code",required=True,)
    desc = fields.Text(string="Description",)
    date_deb = fields.Date(string="Date Début",)
    date_fin = fields.Date(string="Date Fin",)
    etat = fields.Selection(selection=[('0','0.Emis'),('1','1.Non Approuvé'),('2','2.Approuvé'),('3','3.Clôture'),], string="Etat",)
    cree = fields.Datetime('Créé le', required=False, readonly=True
                                , default=lambda self: fields.datetime.now())
    n_di = fields.Char(string="N° DI",)
    createur = fields.Char(string="Créateur",)
    demandeur = fields.Char(string="Demandeur",)
    autorise_par = fields.Char(string="Autorisé par",)
    date_cloture = fields.Date(string="Date Clôture",)


    employe = fields.Many2one('employe', 'Employé',)
    n_ot = fields.Many2one('details_ot', 'N° OT',)
    type_permis = fields.Many2one('type_permis', 'Type Permis')