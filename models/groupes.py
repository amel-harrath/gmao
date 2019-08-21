from odoo import models, fields

class Groupes(models.Model):
    _name = 'groupes'

    code = fields.Char(string="Equipement",required=True,)
    desc = fields.Text(string="Description",)
    zone = fields.Many2one('zone',string="Zone",)
    famille = fields.Many2one('famille', string="Famille")
    c_charge = fields.Char(string="C Charge",)
    fonc = fields.Many2one('fonction', string="Fonction",)
    entite = fields.Many2one('entite', string="Entité")
    type_permis = fields.Char(string="Type Permis",)
    pt_ot_correctif = fields.Boolean(string="PT pour OT Correctf",)
    eqpt_arret = fields.Boolean(string="Equipement Arrêt",)
    resp = fields.Char(string="Responsable",)
    code_barres = fields.Char(string="Code Barres",)
    calcul = fields.Boolean(string="Calcul%",)
    alloc_cout = fields.Selection(selection=[('0','Groupe + C Charges Groupe'),('1','Groupe + C Charges Equipements'),('2','Equipements + C Charges Groupe'),('3','Equipements + C Charges Equipements'),], string="",)
    nb_eqpt = fields.Integer(string="Nb Equipements",)
    priorite = fields.Integer(string="Priorité",)
    hist = fields.Boolean(string="Historique",)
    etat_eqpt = fields.Selection(string="Etat Système",
    selection=[('0','0.Normal'),
    ('1','1.Dégradé'),
    ('2','2.Préparation'),
    ('3','3.Rebus'),
    ('4','4.Consigé'),],)

    eqpts = fields.Many2many('topographie', 'group_eqpt', 'group_id', 'topo_id', string="Equipements" )
    attributs = fields.One2many('attribut','gp_attributs_id','Attribut')
    cout = fields.One2many('cout','gp_cout_id','Cout')
    contrats = fields.Many2many('details_contrats','details_contrats_gp', 'groupe_id', 'contrat_id', string='Contrats',)
    