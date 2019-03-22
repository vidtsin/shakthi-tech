# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Employee Additional Fields",
    "version": "1.1",
    "category": "Employee",
    "website": "http://www.pptservices.com",
	"description": """
		Additional Fields on employees.
    """,
    "author": "PPTS",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
	'hr','base','hr_contract','hr_attendance',
    ],
    "data": [
        'views/hr_views.xml',
    ],
}

