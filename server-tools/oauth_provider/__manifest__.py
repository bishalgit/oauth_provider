# -*- coding: utf-8 -*-
{
    'name': "OAuth Provider for Odoo",

    'summary': """
        Allows to use Odoo as an OAuth2 provider""",

    'description': """
        Allows to use Odoo as an OAuth2 provider
    """,

    'author': "Bishal",
    'license': 'AGPL-3',
    'installable': True,
    'website': "https://bishalgit.github.io/server-tools/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Authentication',
    'version': '11.0.1.1',

    'external_dependancies': {
        'python': ['oauthlib'],
    },
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/oauth_provider_security.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/oauth_provider_client.xml',
        'views/oauth_provider_scope.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/authorize.xml'],
    'pre_init_hook': 'pre_init_hook',
}