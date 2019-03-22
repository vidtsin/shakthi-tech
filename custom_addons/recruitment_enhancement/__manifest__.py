# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Custom HR Recruitment",
    "version": "1.1",
    "category": "Employee",
    "website": "http://www.pptservices.com",
	"description": """
		Custom HR Recruitment.
    """,
    "author": "PPTS",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
	'hr',
    'base',
    'hr_contract',
    'hr_attendance',
    'hr_recruitment',
    'website_hr_recruitment',
    'website_form',
    'employee_additional_fields',
    ],
    "data": [
        'views/recruitment.xml',
    ],
}

