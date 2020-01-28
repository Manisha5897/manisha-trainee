{
    'name': "My Lunch Box",
    'version': '1.0',
    # 'depends': ['base'],
    'depends': ['web_dashboard'],
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
        'report/product_report.xml',
    ],
    'demo': [
        'demo/lb_demo.xml',
    ],
}
