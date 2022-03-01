# -*- coding: utf-8 -*-
{
    'name': "sevenseeds",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/player.xml',
        'views/character_slots.xml',
        'views/views.xml',
        'views/characters.xml',
        'demo/teams.xml',
        'demo/areas.xml',
        'demo/skills.xml',
        'demo/jobs.xml',
        'demo/weapons.xml',
        'demo/character_templates.xml',
        'views/journey.xml',

        'crons/crons.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
