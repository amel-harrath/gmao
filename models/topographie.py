from odoo import models, fields, api

class Topographie(models.Model):
    _name = 'topographie'


    def _get_pays(self):
        pays = ["Afghanistan",
            "Afrique du Sud",
            "Albanie",
            "Algérie",
            "Allemagne",
            "Andorre",
            "Angola",
            "Anguilla",
            "Antarctique",
            "Antigua-et-Barbuda",
            "Antilles néerlandaises",
            "Arabie saoudite",
            "Argentine",
            "Arménie",
            "Aruba",
            "Australie",
            "Autriche",
            "Azerbaïdjan",
            "Bahamas",
            "Bahreïn",
            "Bangladesh",
            "Barbade",
            "Bélarus",
            "Belgique",
            "Belize",
            "Bénin",
            "Bermudes",
            "Bhoutan",
            "Bolivie",
            "Bosnie-Herzégovine",
            "Botswana",
            "Brésil",
            "Brunéi Darussalam",
            "Bulgarie",
            "Burkina Faso",
            "Burundi",
            "Cambodge",
            "Cameroun",
            "Canada",
            "Cap-Vert",
            "Ceuta et Melilla",
            "Chili",
            "Chine",
            "Chypre",
            "Colombie",
            "Comores",
            "Congo-Brazzaville",
            "Corée du Nord",
            "Corée du Sud",
            "Costa Rica",
            "Côte d’Ivoire",
            "Croatie",
            "Cuba",
            "Danemark",
            "Diego Garcia",
            "Djibouti",
            "Dominique",
            "Égypte",
            "El Salvador",
            "Émirats arabes unis",
            "Équateur",
            "Érythrée",
            "Espagne",
            "Estonie",
            "État de la Cité du Vatican",
            "États fédérés de Micronésie",
            "États-Unis",
            "Éthiopie",
            "Fidji",
            "Finlande",
            "France",
            "Gabon",
            "Gambie",
            "Géorgie",
            "Géorgie du Sud et les îles Sandwich du Sud",
            "Ghana",
            "Gibraltar",
            "Grèce",
            "Grenade",
            "Groenland",
            "Guadeloupe",
            "Guam",
            "Guatemala",
            "Guernesey",
            "Guinée",
            "Guinée équatoriale",
            "Guinée-Bissau",
            "Guyana",
            "Guyane française",
            "Haïti",
            "Honduras",
            "Hongrie",
            "Île Bouvet",
            "Île Christmas",
            "Île Clipperton",
            "Île de l'Ascension",
            "Île de Man",
            "Île Norfolk",
            "Îles Åland",
            "Îles Caïmans",
            "Îles Canaries",
            "Îles Cocos - Keeling",
            "Îles Cook",
            "Îles Féroé",
            "Îles Heard et MacDonald",
            "Îles Malouines",
            "Îles Mariannes du Nord",
            "Îles Marshall",
            "Îles Mineures Éloignées des États-Unis",
            "Îles Salomon",
            "Îles Turks et Caïques",
            "Îles Vierges britanniques",
            "Îles Vierges des États-Unis",
            "Inde",
            "Indonésie",
            "Irak",
            "Iran",
            "Irlande",
            "Islande",
            "Israël",
            "Italie",
            "Jamaïque",
            "Japon",
            "Jersey",
            "Jordanie",
            "Kazakhstan",
            "Kenya",
            "Kirghizistan",
            "Kiribati",
            "Koweït",
            "Laos",
            "Lesotho",
            "Lettonie",
            "Liban",
            "Libéria",
            "Libye",
            "Liechtenstein",
            "Lituanie",
            "Luxembourg",
            "Macédoine",
            "Madagascar",
            "Malaisie",
            "Malawi",
            "Maldives",
            "Mali",
            "Malte",
            "Maroc",
            "Martinique",
            "Maurice",
            "Mauritanie",
            "Mayotte",
            "Mexique",
            "Moldavie",
            "Monaco",
            "Mongolie",
            "Monténégro",
            "Montserrat",
            "Mozambique",
            "Myanmar",
            "Namibie",
            "Nauru",
            "Népal",
            "Nicaragua",
            "Niger",
            "Nigéria",
            "Niue",
            "Norvège",
            "Nouvelle-Calédonie",
            "Nouvelle-Zélande",
            "Oman",
            "Ouganda",
            "Ouzbékistan",
            "Pakistan",
            "Palaos",
            "Panama",
            "Papouasie-Nouvelle-Guinée",
            "Paraguay",
            "Pays-Bas",
            "Pérou",
            "Philippines",
            "Pitcairn",
            "Pologne",
            "Polynésie française",
            "Porto Rico",
            "Portugal",
            "Qatar",
            "R.A.S. chinoise de Hong Kong",
            "R.A.S. chinoise de Macao",
            "régions éloignées de l’Océanie",
            "République centrafricaine",
            "République démocratique du Congo",
            "République dominicaine",
            "République tchèque",
            "Réunion",
            "Roumanie",
            "Royaume-Uni",
            "Russie",
            "Rwanda",
            "Sahara occidental",
            "Saint-Barthélémy",
            "Saint-Kitts-et-Nevis",
            "Saint-Marin",
            "Saint-Martin",
            "Saint-Pierre-et-Miquelon",
            "Saint-Vincent-et-les Grenadines",
            "Sainte-Hélène",
            "Sainte-Lucie",
            "Samoa",
            "Samoa américaines",
            "Sao Tomé-et-Principe",
            "Sénégal",
            "Serbie",
            "Serbie-et-Monténégro",
            "Seychelles",
            "Sierra Leone",
            "Singapour",
            "Slovaquie",
            "Slovénie",
            "Somalie",
            "Soudan",
            "Sri Lanka",
            "Suède",
            "Suisse",
            "Suriname",
            "Svalbard et Île Jan Mayen",
            "Swaziland",
            "Syrie",
            "Tadjikistan",
            "Taïwan",
            "Tanzanie",
            "Tchad",
            "Terres australes françaises",
            "Territoire britannique de l'océan Indien",
            "Territoire palestinien",
            "Thaïlande",
            "Timor oriental",
            "Togo",
            "Tokelau",
            "Tonga",
            "Trinité-et-Tobago",
            "Tristan da Cunha",
            "Tunisie",
            "Turkménistan",
            "Turquie",
            "Tuvalu",
            "Ukraine",
            "Union européenne",
            "Uruguay",
            "Vanuatu",
            "Venezuela",
            "Viêt Nam",
            "Wallis-et-Futuna",
            "Yémen",
            "Zambie",
            "Zimbabwe"]
        pays_list=[]
        for i in pays:
            pays_list.append((i, i))
        return pays_list

    

    
    equipement = fields.Many2one('equipement', string="Equipement", required=True)
    prefixe = fields.Selection(selection=[('bat1','BAT1'),('prod1','PROD1'),('s1','S1'),('s2','S2'),('siv','SIV'),])
    description = fields.Text(string="Description", related='equipement.desc',)
    zone = fields.Many2one('zone',string="Zone", related='equipement.zone')
    type_permis = fields.Char(string="Type Permis",)
    parent_geo = fields.Char(string="Parent Géograph.",related="equipement.parent_geo",)
    etat_equip = fields.Selection(string="Etat Equipement", related="equipement.etat_eqpt",)
    niveau = fields.Integer(string="Niveau", min="1",related="equipement.niv", default="1")
    famille = fields.Char(string="Famille",related="equipement.famille",)
    c_charge = fields.Char(string="C Charge",related="equipement.c_charge",)
    fonc = fields.Many2one('fonction', string="Fonction",related="equipement.fonc",)
    pt_ot_correctif = fields.Boolean(string="PT pour OT Correctf",)
    entite = fields.Many2one('entite', string="Entité",)
    n_eqpt = fields.Integer(string="N° Equipement",)
    eqpt_arret = fields.Boolean(string="Equipement Arrêt",)
    cat = fields.Selection(string=" ", related="equipement.type_eqpt",)
    modele = fields.Boolean(string="Modèle?",)
    code_barres = fields.Char(string="Code Barres",)
    utilisateur = fields.Char(string="Utilisateur",)
    resp = fields.Char(string="Responsable",)
    emp = fields.Char(string="Emplacement",)
    tel = fields.Integer(string="Téléphone",)
    type_containeur = fields.Char(string="Type Containeur",)
    modele_eqpt = fields.Char(string="Modèle Equipement",)
    typ = fields.Char(string="Type",)
    article = fields.Char(string="Article",)
    cmpt_article = fields.Integer(sring="Compteur Article")
    sys = fields.Char(string="Systéme",)
    priorite = fields.Integer(string="Priorité",)
    index = fields.Char(string="Index Structure",)
    hist = fields.Boolean(string="Historique",)
    remarque = fields.Text()
    n_modele = fields.Char(string="N° Modèle",)
    constructeur = fields.Char(string="Constructeur",)
    fournisseur = fields.Char(string="Fournisseur",)
    capacite = fields.Char(string="Capacité",)
    alimentation = fields.Char(string="Alimentation",)
    compteur_specification = fields.Many2one('compteur', string="Compteur",)
    mtbf = fields.Integer(string="MTBF",)
    mttr = fields.Float(string="MTTR",)
    article = fields.Char(string="Article",)
    n_serie = fields.Char(string="N° Série",)
    construction = fields.Date(string="Construction",)
    arrive = fields.Date(string="Arrivé",)
    duree_vie_min_mm = fields.Integer(string="",)
    duree_vie_min_aa = fields.Integer(string="",)
    compteur_duree_min = fields.Integer(string="Compteur",)
    duree_vie_max_mm = fields.Integer(string="",)
    duree_vie_max_aa = fields.Integer(string="",)
    compteur_duree_max = fields.Integer(string="Compteur",)
    n_enregistrement = fields.Char(string="N° Enregistrement",)
    pays = fields.Selection('_get_pays', string="Pays",)
    #Conteneur
    haut_ext = fields.Float(string="Hauteur Extérieure",)
    largeur_ext = fields.Float(string="Largeur Extérieure",)
    long_ext = fields.Float(string="Longueur Extérieure",)
    long_porte = fields.Float(string="Longueur Porte",)
    poids_a_vide = fields.Float(string="Poids à Vide",)
    surface = fields.Float(string="Surface",)
    facteur_k_francais = fields.Float(string="Facteur K Français",)
    poids_brut = fields.Float(string="Poids Brut",)
    haut_int = fields.Float(string="Hauteur Intérieure",)
    largeur_int = fields.Float(string="Largeur Intérieure",)
    long_int = fields.Float(string="Longueur Intérieure",)
    larg_porte = fields.Float(string="Largeur Porte",)
    charge_maxi = fields.Float(string="Charge Maxi",)
    volume = fields.Float(string="Volume",)
    facteur_f_allemand = fields.Float(string="Facteur K Allemand",)
    size16 = fields.Float(string="Size 16",)
    #Etalonnage
    per_nominale = fields.Integer(string="Périodicité Nominale",)
    tps_fonct = fields.Integer(string="Tps de fonctionnement",)
    tps_fonct_avan = fields.Integer(string="Tps de fonctionnement avan",)
    nb_util_avant_etalonn = fields.Integer(string="Nb utilisations avant étalonn",)
    nb_util_apres_etalonn = fields.Integer(string="Nb utilisations apres étalonn",)
    act_radio_all = fields.Integer(string="Activ. Radio. Allemande",)
    act_radio_ind_fr = fields.Integer(string="Activ. Radio. Ind. Français",)
    dern_pv_etalonn = fields.Integer(string="Dern. PV Etalonnage",)
    per_max = fields.Integer(string="Périodicité Maximum",)
    unite_tps_fonct = fields.Selection(selection=[('0','0.Jour(s)'),('1','1.Mois'),('2','2.Année(s)'),], string="Unité tps de fonctionnement",)
    date_fin_validite = fields.Date(string="Date Fin Validité",)
    nb_util = fields.Integer(string="Nb Utilisation",)
    nb_util_periodique = fields.Integer(string="Nb Utilisations Périodique")
    act_radio_fr = fields.Integer(string="Activ. Radio. Français",)
    act_radio_ind_all = fields.Integer(string="Activ. Radio. Ind. Allemande",)
    contamine = fields.Boolean(string="Contaminé",)



    mouvement = fields.One2many('mouvement', 'equipement_id', 'Mouvement')
    cout = fields.One2many('cout','equipement_cout_id','Cout')
    reparable = fields.One2many('reparable','eqpt_reparable_id','Reparable')
    attributs = fields.One2many('attribut','eqpt_attributs_id','Attribut')

    pieces_outils = fields.One2many('pieces_outils', 'equipement_id', 'Pieces_Outils')
    piece = fields.One2many('details_pieces',string='topo',related="pieces_outils.piece")

    contrat_rel = fields.One2many('contrat','equipement_id',   string='Contrats', )
    contrats = fields.One2many('details_contrats',string="Contrats", related="contrat_rel.details_contrat", readonly=True, domain="[('type_ct', '=','0'),('type_ct','=','1')]",)


    gps = fields.One2many('group','eqpts', string="Groupes" )
    alimente = fields.Many2many('equipement', 'alimente_eqpt', 'topo_id', 'eqpt_alimente_id', string="Alimente",)
    alimente_par = fields.Many2many('equipement', 'alimente_par_eqpt', 'topo_id', 'eqpt_alim_par_id', string="Alimenté Par",)
    structure_tech = fields.Many2many('equipement', 'structure_tech', 'topo_id', 'eqpt_struct_id', string="Structure Technique",)
    equivalents = fields.Many2many('equipement', 'equivalant', 'topo_id', 'equivt_id', string="Equivalant", domain="[('fonc','=','topographie.fonc')]",)
    compteur = fields.Many2many('compteur', 'compteur_eqpt', 'topo_id', 'cmpt_id', string="Compteur",)
    