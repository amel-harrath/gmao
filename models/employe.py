from odoo import models, fields

class Employe(models.Model):
    _name = 'employe'


    mat = fields.Integer(string="Matricule", required=True,)
    ressource = fields.Char(string="Ressource",)
    superv = fields.Char(string="Superviseur",)
    entite = fields.Many2one('entite', string="Entite",)

    code_barres = fields.Char(string="Code Barres",)
    c_charge = fields.Char(string="C. Charge",)
    n_eq = fields.Integer(string="N° Equipe",)
    hrs_payees_jrs = fields.Integer(string="Hrs Payées/Jour",)
    hrs_eff_jrs = fields.Integer(string="Hrs Effectives/Jour",)
    date_ref = fields.Date(string="Date Référence",)
    taille_model = fields.Integer(string="Taille Model",)
    type_cout = fields.Selection(selection=[('0','0.Interne'),('1','1.Externe'),], string="Type Coût",)
    date_entree = fields.Date(string="Date Entrée",)
    fin_contrat = fields.Date(string="Fin Contrat",)
    n_sec_soc = fields.Char(string="N° Sécurité Sociale",)
    contact_urgence = fields.Char(string="Contact Urgence",)
    tel = fields.Char(string="Téléphone",)
    fax = fields.Char(string="Fax",)
    email = fields.Char(string="Email",)
    texte1 = fields.Text(string="Texte 1",)
    permanent = fields.Boolean(string="Permanent",)