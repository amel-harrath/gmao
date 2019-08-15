from odoo import models, fields, api

class Cout(models.Model):
    _name = 'cout'

    _sql_constraints = [
        ('unique_zone_year_type_combo', 'unique(zone_cout_id, periode, type_cout )', ("Les côut pour  cette année et le type déjà existent!\n ")),
        ('unique_func_year_type_combo', 'unique(fonction_cout_id, periode, type_cout )', ("Les côut pour cette année et ce type déjà existent!\n ")),

            ]

    
    def _calcul_total_ressource(self):
        for cout in self:
            cout.ressource_total = cout.ressource_correctif + cout.ressource_planifie + cout.ressource_divers
            
    def _calcul_total_materiel(self):
        for cout in self:
            cout.materiel_total = cout.materiel_correctif + cout.materiel_planifie + cout.materiel_divers
    
    def _calcul_total_deplacement(self):
        for cout in self:
            cout.deplacement_total = cout.deplacement_correctif + cout.deplacement_planifie + cout.deplacement_divers

    def _calcul_total_moyen(self):
        for cout in self:
            cout.moyen_total = cout.moyen_correctif + cout.moyen_planifie + cout.moyen_divers

    def _calcul_total_ajustement(self):
        for cout in self:
            cout.ajustement_total = cout.ajustement_correctif + cout.ajustement_planifie + cout.ajustement_divers

    def _calcul_total_autre(self):
        for cout in self:
            cout.autre_total = cout.autre_correctif + cout.autre_planifie + cout.autre_divers
    
    def _calcul_total(self):
        for cout in self:
            cout.total_total = cout.ressource_total + cout.materiel_total + cout.deplacement_total + cout.moyen_total + cout.ajustement_total + cout.autre_total

    def _calcul_per_ressource(self):
        for cout in self:
            if cout.total_total != 0:
                cout.ressource_percent = (cout.ressource_total / cout.total_total) * 100 
            else:
                cout.ressource_percent = 0

    def _calcul_per_materiel(self):
        for cout in self:
            if cout.total_total != 0:
                cout.materiel_percent = (cout.materiel_total / cout.total_total) * 100 
            else:
                cout.materiel_percent = 0

    def _calcul_per_deplacement(self):
        for cout in self:
            if cout.total_total != 0:
                cout.deplacement_percent = (cout.deplacement_total / cout.total_total) * 100 
            else:
                cout.deplacement_percent = 0

    def _calcul_per_moyen(self):
        for cout in self:
            if cout.total_total != 0:
                cout.moyen_percent = (cout.moyen_total / cout.total_total) * 100 
            else:
                cout.moyen_percent = 0

    def _calcul_per_ajustement(self):
        for cout in self:
            if cout.total_total != 0:
                cout.ajustement_percent = (cout.ajustement_total / cout.total_total) * 100 
            else:
                cout.ajustement_percent = 0

    def _calcul_per_autre(self):
        for cout in self:
            if cout.total_total != 0:
                cout.autre_percent = (cout.autre_total / cout.total_total) * 100 
            else:
                cout.autre_percent = 0

    def _calcul_total_planifie(self):
        for cout in self:
            cout.total_planifie = cout.ressource_planifie + cout.materiel_planifie + cout.deplacement_planifie + cout.moyen_planifie + cout.ajustement_planifie + cout.autre_planifie

    def _calcul_total_correctif(self):
        for cout in self:
            cout.total_correctif = cout.ressource_correctif + cout.materiel_correctif + cout.deplacement_correctif + cout.moyen_correctif + cout.ajustement_correctif + cout.autre_correctif
    
    def _calcul_total_divers(self):
        for cout in self:
            cout.total_divers = cout.ressource_divers + cout.materiel_divers + cout.deplacement_divers + cout.moyen_divers + cout.ajustement_divers + cout.autre_divers

    def _calcul_per_planifie(self):
        for cout in self:
            if cout.total_total != 0:
                cout.per_planifie = (cout.total_planifie / cout.total_total) * 100
            else:
                cout.per_planifie = 0

    def _calcul_per_correctif(self):
        for cout in self:
            if cout.total_total != 0:
                cout.per_correctif = (cout.total_correctif / cout.total_total) * 100
            else:
                cout.per_correctif = 0

    def _calcul_per_divers(self):
        for cout in self:
            if cout.total_total != 0:
                cout.per_divers = (cout.total_divers / cout.total_total) * 100
            else:
                cout.per_divers = 0

    def _calcul_total_nbot(self):
        for cout in self:
            cout.nbot_total = cout.nbot_correctif + cout.nbot_planifie + cout.nbot_divers
    
    def _calcul_total_tempsarret(self):
        for cout in self:
            cout.tpsarret_total = cout.tpsarret_planifie + cout.tpsarret_correctif + cout.tpsarret_divers

    def _calcul_total_perteprod(self):
        for cout in self:
            cout.perteprod_total = cout.perteprod_correctif + cout.perteprod_planifie + cout.perteprod_divers
    
    def _get_years(self):
        year_list = []
        for i in range(2019, 2999):
            year_list.append((str(i), str(i)))
        return year_list


    zone_cout_id = fields.Many2one('gmao.zone','Zone', invisible=True,)
    fonction_cout_id = fields.Many2one('gmao.fonction','Fonction', invisible=True,)
    equipement_cout_id = fields.Many2one('gmao.equipement', 'Equipement', invisible=True,)
    gp_cout_id = fields.Many2one('gmao.groupe', 'Groupe', invisible=True,)


    periode = fields.Selection( '_get_years', string='Période', default="2019")
    type_cout = fields.Selection(selection=[('interne','Interne'),('externe','Externe'),('total','Total'),], string=" ",)
    ressource_planifie = fields.Float(string='Planifié',)
    ressource_correctif = fields.Float(string='Correctif',)
    ressource_divers = fields.Float(string='Divers',)
    ressource_total = fields.Float(compute='_calcul_total_ressource', string='Total', store=False,)
    ressource_percent = fields.Float(compute='_calcul_per_ressource', string='%', store=False,)
    materiel_planifie = fields.Float(string='Planifié',)
    materiel_correctif = fields.Float(string='Correctif',)
    materiel_divers = fields.Float(string='Divers',)
    materiel_total = fields.Float(compute='_calcul_total_materiel', string='Total', store=False,)
    materiel_percent = fields.Float(compute='_calcul_per_materiel', string='%', store=False,)
    deplacement_planifie = fields.Float(string='Planifié',)
    deplacement_correctif = fields.Float(string='Correctif',)
    deplacement_divers = fields.Float(string='Divers',)
    deplacement_total = fields.Float(compute='_calcul_total_deplacement', string='Total', store=False,)
    deplacement_percent = fields.Float(compute='_calcul_per_deplacement', string='%', store=False,)
    moyen_planifie = fields.Float(string='Planifié',)
    moyen_correctif = fields.Float(string='Correctif',)
    moyen_divers = fields.Float(string='Divers',)
    moyen_total = fields.Float(compute='_calcul_total_moyen', string='Total', store=False,)
    moyen_percent = fields.Float(compute='_calcul_per_moyen', string='%', store=False,)
    ajustement_planifie = fields.Float(string='Planifié',)
    ajustement_correctif = fields.Float(string='Correctif',)
    ajustement_divers = fields.Float(string='Divers',)
    ajustement_total = fields.Float(compute='_calcul_total_ajustement', string='Total', store=False,)
    ajustement_percent = fields.Float(compute='_calcul_per_ajustement', string='%', store=False,)
    autre_planifie = fields.Float(string='Planifié',)
    autre_correctif = fields.Float(string='Correctif',)
    autre_divers = fields.Float(string='Divers',)
    autre_total = fields.Float(compute='_calcul_total_autre', string='Total', store=False,)
    autre_percent = fields.Float(compute='_calcul_per_autre', string='%', store=False,)
    total_planifie = fields.Float(compute='_calcul_total_planifie',string='Total Planifié', store=False,)
    total_correctif = fields.Float(compute='_calcul_total_correctif',string='Total Correctif', store=False,)
    total_divers = fields.Float(compute='_calcul_total_divers',string='Total Divers', store=False,)
    total_total = fields.Float(compute='_calcul_total', string='Total', store=False,)
    per_planifie = fields.Float(compute='_calcul_per_planifie', string='%', store=False,)
    per_correctif = fields.Float(compute='_calcul_per_correctif', string='%', store=False,)
    per_divers = fields.Float(compute='_calcul_per_divers', string='%', store=False,)
    nbot_planifie = fields.Float(string='Planifié',)
    nbot_correctif = fields.Float(string='Correctif',)
    nbot_divers = fields.Float(string='Divers',)
    nbot_total = fields.Float(compute='_calcul_total_nbot', string='Total Nb OT', store=False,)
    tpsarret_planifie = fields.Integer(string='Planifié',)
    tpsarret_correctif = fields.Integer(string='Correctif',)
    tpsarret_divers = fields.Integer(string='Divers',)
    tpsarret_total = fields.Integer(compute='_calcul_total_tempsarret', string='Total Temps Arrêt', store=False,)
    perteprod_planifie = fields.Float(string='Planifié',)
    perteprod_correctif = fields.Float(string='Correctif',)
    perteprod_divers = fields.Float(string='Divers',)
    perteprod_total = fields.Float(compute='_calcul_total_perteprod', string='Total Perte Prod.', store=False,)
    demint_planifie = fields.Float(string='Planifié',)
    demint_correctif = fields.Float(string='Correctif',)
    demint_divers = fields.Float(string='Divers',)


