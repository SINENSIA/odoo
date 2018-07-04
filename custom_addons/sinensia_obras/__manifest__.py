# -*- coding: utf-8 -*-
{
    'name': "sinensia_obras",

    'summary': """
        Modulo para controlar obras
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Este módulo se encarga de gestionar todas las obras y sus proyectos
    """,

    'author': "SINENSIA IT SOLUTIONS",
    'website': "https://www.sinensia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'hr_expense', 'hr_timesheet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}