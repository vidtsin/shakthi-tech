# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Employee Training Management',
    'version': '1.1',
    'website' : 'http://www.pptssolutions.com',
    'category': 'hr',
    'depends' : ['base','hr'],
    'description': """
        Training schedule for employee
    """,
    'data': [
        
        'views/employee_training_views.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'application':True
}
