from odoo import models, fields

class Details_contrats(models.Model):
    _name = 'details_contrats'

    code = fields.Char(string="Contrat",required=True,)
    desc = fields.Text(string="Description",)
    ss_traitant = fields.Char(string="Sous-Traitant",)
    etat = fields.Selection(selection=[('0','0.Ouvert'),('1','1.Annuel'),], string="Etat",)
    type_ct = fields.Selection(selection=[('0','0.Commande Ouverte'),('1','1.Annuel'),('2','2.Client'),], string="Type",)
    entite = fields.Many2one('entite', string="Entité",)
    valeur = fields.Integer(string="Valeur",)
    date_deb = fields.Date(string="Date Déb.",)
    date_fin = fields.Date(string="Date Fin",)
    val_max = fields.Integer(string="Valeur Maxi")
    val_min = fields.Integer(string="Valeur Mini")
    total_nb_ot = fields.Integer(string="Total Nb OT",)
    tot_hrs_travaillees = fields.Integer(string="Total Hrs Travaillées",)
    delai_intr_min = fields.Integer(string="Délai Intervention Min",)
    delai_intr_max = fields.Integer(string="Délai Intervention Max",)
    delai_intr_moy = fields.Integer(string="Délai Intervention Moyen",)
    tps_repar_min = fields.Integer(string="Temps de répartition Min",)
    tps_repar_max = fields.Integer(string="Temps de répartition Max",)
    tps_repar_moy = fields.Integer(string="Temps de répartition Moy",)



    groupes_ids = fields.Many2many('groupes','details_contrats_gp','contrat_id','groupe_id','Contrats Groupes')
    contrat_eqpts_id = fields.Many2many('contrat', 'contrat_eqpts','details_contrat_id','contrat_eqpt_id',)
    topo_id = fields.Many2one('topographie', related="contrat_eqpts_id.equipement_id",)