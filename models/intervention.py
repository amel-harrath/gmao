from odoo import models, fields

class Intervention(models.Model):
	_name = 'intervention'
	_description='description of intervention'

	intr_code = fields.Integer(string='Intervention',required=True,)
	description = fields.Text(string='Description')
	intr_type = fields.Char(string='Type',)
	entite = fields.Many2one('entite', string='Entité',)
	planification= fields.Selection(selection=[('0','0.Juste à temps'),
	('1','1.Date de début'),
	('2','2.Date de fin'),
	('3','3.Intervalle Fixe'),
	('4','4.Arrêt'),
	('5','5.Régulier'),
	('6','6.Mensuel/Annuel'),
	('7','7.Prédéfini'),],
	string="Planification", default='7',)
	jours_ouvres = fields.Selection(selection=[('0','0.Non utilisé'),
	('1','1.Fréquence + Date'),
	('2','2.Date'),],
	string="Jours Ouvrés", default='0',)
	indicateur = fields.Char(string='Indicateur',)
	intr_fille = fields.Char(string='Intervention Fille',)
	descp_fils = fields.Text(string='Description Fils',)
	multiplicite = fields.Char(string='Multiplicité',)
	parent_critique = fields.Boolean(string='Parent Critique',)
	code_parent = fields.Char(string='Code Parent',)
	desc_parent = fields.Text(string='Description Parent',)


	equipement_ids = fields.One2many('topographie', 'intervention_id','Equipements',)
	ressources_ids = fields.One2many('ressources','intervention_id','Ressources',)
	famille_ids = fields.Many2many('famille','intervention_famille','intervention_id','famille_id',string='Famille',)