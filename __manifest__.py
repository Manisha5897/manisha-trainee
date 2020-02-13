{
    'name': "My Lunch Box",
    'depends': ['web_dashboard', 'portal'],
    'description': """
    This is my lunch box application
    """,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/lb_data.xml',
        'views/views.xml',
        # 'wizard/cust_wizard.xml',
        # 'views/templates.xml',
        'views/portal_template.xml',
        'report/product_report.xml',
    ],
    'demo': [
        'demo/lb_demo.xml',
    ],
}
