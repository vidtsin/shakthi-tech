# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Employee Expense Management',
    'version': '1.1',
    'website' : 'http://www.pptssolutions.com',
    'category': 'expense',
    'depends' : ['base','hr_expense'],
    'description': """
       Expense Management for employee
    """,
    'data': [
        
        'views/employee_grade_master_views.xml',
        'views/hr_views.xml',
        'views/employee_expense_views.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'application':True
}
