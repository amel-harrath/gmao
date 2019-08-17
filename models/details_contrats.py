from odoo import models, fields

class Details_contrats(models.Model):
    _name = 'details_contrats'

    code = fields.Char(string="Contrat",)
    desc = fields.Text(string="Description",)
    ss_traitant = fields.Char(string="Sous-Traitant",)
    etat = fields.Selection(selection=[('0','0.Ouvert'),('1','1.Annuel'),], string="Etat",)
    type_ct = fields.Selection(selection=[('0','0.Commande Ouverte'),('1','1.Annuel'),('2','2.Autres'),], string="Type",)
    entite = fields.Many2one('entite', string="Entité",)
    valeur = fields.Float(string="Valeur",)
    date_deb = fields.Date(string="Date Déb.",)

    contrat_eqpts_id = fields.Many2one('contrat', 'Contrats')