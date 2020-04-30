# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        For managing all kinds of hospitals""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/patient_sequence.xml',
        'data/data.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/report_patient_card.xml',
        'reports/report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

