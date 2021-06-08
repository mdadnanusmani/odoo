# -*- coding: utf-8 -*-
{
    'name': "account_group_hierarchy",

    'summary': """
        Chart of account groups and parent of Account Groups""",

    'description': """
        Account Groups Hierarchy and Account Types
    """,

    'author': "Adnan Usmani",
    'website': "http://www.pharmola.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '14.0.1',
    'license': 'LGPL-3',

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
'images': [
'static/description/banner.PNG',
'static/description/icon.PNG',
'static/description/image1.PNG',
'static/description/image2.PNG',
'static/description/image3.PNG',
'static/description/image4.PNG',

],
}
