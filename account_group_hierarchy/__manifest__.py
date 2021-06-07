# -*- coding: utf-8 -*-
{
    'name': "account_group_hierarchy",

    'summary': """
        Chart of account groups and parent of COA groups""",

    'description': """
        Chart of account groups and parent of COA groups
    """,

    'author': "Adnan Usmani",
    'website': "http://www.pharmola.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

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
