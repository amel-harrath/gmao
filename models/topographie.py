from odoo import models, fields

class Topographie(models.Model):
    _name = 'topographie'


    #def on_change_zone(self,cr,uid,ids,equipement, contexte=None):
     #   val = {}
      #  if not equipement:
       #     return {}
        #zones = self.pool.get('equipement')
        #zone = zones.browse(cr,uid,equipement,contexte=None)
        #val.update({'zone':zone})
        #return {'value':val} 

    equipement = fields.Many2one('equipement', string="Equipement", required=True)
    description = fields.Text(string="Description", related='equipement.desc',)
    zone = fields.Many2one('zone',string="Zone", related='equipement.zone')
    type_permis = fields.Char(string="Type Permis",)
    parent_geo = fields.Char(string="Parent Géograph.",)
    etat_equip = fields.Char()
    niveau = fields.Integer(string="Niveau", max="100", min="0",)
    famille = fields.Char(string="Famille",)
    c_charge = fields.Char(string="C Charge",)
    fonc = fields.Char(string="Fonction",)
    pt_ot_correctif = fields.Boolean(string="PT pour OT Correctf",)
    entite = fields.Char(string="Entité",)
    n_eqpt = fields.Integer(string="N° Equipement",)
    eqpt_arret = fields.Boolean(string="Equipement Arrêt",)
    cat = fields.Selection(selection=[('0','0.Technique'),('1','1.Géographique'),], string=" ",)
