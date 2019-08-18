from odoo import models, fields, api

class Details_OT(models.Model):
    _name = 'details_ot'


    def _get_cout_total(self):
        for cout in self:
            cout.cout_total = cout.cout_ress_ext + cout.cout_ress_int + cout.ressources + cout.pieces + cout.autres + cout.moyens + cout.frais_dep + cout.ajustement

    @api.model
    def create(self, vals):
        vals['num_ot'] = self.env['ir.sequence'].next_by_code('increment_num_ot')
        res = super(Details_OT, self).create(vals)
        return res

    num_ot = fields.Integer(string='N° OT', required=True, copy=False, readonly=True, index=True,)
    equipement = fields.Many2one('topographie', string="Equipement",required=True,)
    desc_eqpt = fields.Text(string="", related="equipement.description",)
    intervention = fields.Char(string="Intervention",required=True,)
    type_intr = fields.Char(string="Type",required=True,)
    classe = fields.Char(string="Classe",)
    priorite = fields.Char(string="Priorité",)
    etat_ot = fields.Selection(selection=[('1','1.Crée'),], string="Etat OT", required=True,)
    date_prevue = fields.Date(string="Date Prévue",required=True,)
    desc_inter = fields.Char(string="",)
    cat_ot = fields.Selection(selection=[('equipement','Equipement'),('famille','Famille'),], string="",)
    superviseur = fields.Char(string="Superviseur",)
    c_charge = fields.Char(string="C. Charge",required=True,)
    etat_eqpt = fields.Char(string="Etat Equipement",)
    criticite = fields.Selection(selection=[('0','0.Normal'),], string="Criticié",)

    fin_prevue = fields.Date(string="Fin Prévue",)
    date_deb = fields.Datetime(string="Date Début",)
    date_fin = fields.Datetime(string="Date Fin",)
    unite_cumulees = fields.Integer(string="Unité Cumulées",)
    hrs_realisees = fields.Integer(string="Hrs Réalisées",)
    hrs_planifiees = fields.Integer(string="Hrs Planifiées",)
    ot_pere = fields.Many2one('details_ot', string="OT Père",)
    n_plan = fields.Char(string="N° Plan",)
    n_di = fields.Char(string="N° DI",)
    signe_par = fields.Char(string="Signé Par",)
    date_rapport = fields.Datetime(string="Date Rapport",)
    date_declaration = fields.Datetime(string="Date de Déclaration",)
    tel_rapport = fields.Char(string="Tél Rapport",)
    eqpt_ss_ctr = fields.Boolean(string="Sauter Equip. Sous Contrat",)
    allo_empl = fields.Boolean(string="Allouer Employés",)
    verif_qualifs = fields.Boolean(string="Vérif. Qualifications",)
    cout_ress_ext = fields.Integer(string="Coût Ress. Externe",)
    cout_ress_int = fields.Integer(string="Coût Ress. Interne",)
    ressources = fields.Integer(string="Ressources",)
    pieces = fields.Integer(string="Pièces",)
    autres = fields.Integer(string="Autres",)
    moyens = fields.Integer(string="Moyens",)
    frais_dep = fields.Integer(string="Frais de déplacement",)
    ajustement = fields.Integer(string="Ajustement",)
    cout_total = fields.Integer(string="Coût Total", compute="_get_cout_total",)
    reparable = fields.Boolean(string="Réparable",)
    permis_travail = fields.Many2one('permis_travail', string="Permis Travail",)
    cpt = fields.Many2one('compteur', string="Compteur",)
    desc_cpt = fields.Text(string='', related="cpt.desc",)
    valeur_cpt = fields.Char(string="Valeur Compteur",)
    tps_arret = fields.Integer(string="Tps Arrêt",)
    perte_prod  = fields.Integer(string="Perte Prod.",)
    type_ot = fields.Selection(selection=[('1','1.Non Planifié'),], string="Type OT",)
    maj_direct_releve = fields.Boolean(string="MàJ directe Relevé",)
    replan_auto = fields.Boolean(string="Replanif. Auto",)
    redond = fields.Boolean(string="Redondance",)
    anc_occ = fields.Selection(selection=[('0','Effacer'),('1','Déplacer'),], string="Anc. Occurrences",)
    contrat = fields.Many2one('details_contrats', string="Contrat",)
    type_contrat = fields.Selection(string="Type Contrat", related="contrat.type_ct",)
    type_cout = fields.Selection(selection=[('interne','Interne'),('externe','Externe'),('total','Total'),], string="Type Coût",)
    rep_eqpt = fields.Char(string="Rép. Eqpt",)
    nouv_rep = fields.Char(string="Nouv. Rep",)
    projet = fields.Char(string='Projet',)
    zone = fields.Many2one('zone',string="Zone",)
    devis = fields.Char(string="Devis",)
    demande_par = fields.Char(string="Demandé par",)
    realise_par = fields.Char(string="Réalisé par",)
    sec_verif = fields.Boolean(string="Sécurité à vérifier",)
    n_serie = fields.Char(string="N° Série",)
    nouv_n_serie = fields.Char(string="Nouveau N° Série",)
    tel_eqpt = fields.Char(string="Tél Equipement",)
    fonction = fields.Many2one('fonction', string="Fonction",)



    afaire = fields.Many2many('details_consignes','consignes_afaire_details_ot','details_ot_id','consignes_id', 'A Faire',)
    anepasfaire = fields.Many2many('details_consignes','consignes_anepasfaire_details_ot','details_ot_id','consignes_id', 'A ne pas Faire',)
    allocation_employes_ids = fields.One2many('allocation_employeot', 'details_ot_ids', 'Allocation Employés')
    allocation_ressources_ids = fields.One2many('allocation_ressourcesot', 'details_ot_ids','Allocation Ressources')
    commentaires_ids = fields.One2many('commentaires_ot', 'details_ot_ids','Commentaires')
    defauts = fields.One2many('defauts', 'ot_id', 'Defauts')
    compteur_ids = fields.One2many('compteur','ot_id','Compteurs',)
