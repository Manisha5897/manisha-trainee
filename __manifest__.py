{
    'name': "My Lunch Box",
    'version': '1.0',
    'depends': ['base', 'website'],
    'description': """
    This is my lunch box application
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/cust_wizard.xml',
        'views/templates.xml',
        'report/product_report.xml',
    ],
    'demo': [
        'demo/lb_demo.xml',
    ],
}