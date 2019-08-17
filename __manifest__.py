# -*- coding: utf-8 -*-
{
    'name': "GMAO",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Maintenance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employe.xml',
        'views/details_contrats.xml',
        'views/defauts.xml',
        'views/consignes.xml',
        'views/details_consignes.xml',
        'views/manuels_dessins.xml',
        'views/details_dessins.xml',
        'views/group.xml',
        'views/pieces_outils.xml',
        'views/contrat.xml',
        'views/zone.xml',
        'views/attribut.xml',
        'views/compteur.xml',
        'views/reparable.xml',
        'views/mouvement.xml',
        'views/details_pieces.xml',
        'views/cout.xml',
        'views/intervention.xml',
        'views/eqpt_intervention.xml',
        'views/equipement.xml',
        'views/fonction.xml',
        'views/topographie.xml',
        'views/views.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}