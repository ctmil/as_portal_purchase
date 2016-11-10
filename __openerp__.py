# -*- coding: utf-8 -*-
{
    'name': 'Portal Purchase',
    'version': '0.1',
    'category': 'Purchase',
    'depends': ['purchase', 'portal'],
    'data': [
        'security/portal_security.xml',
        'portal_purchase_view.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'category': 'Hidden',
}
