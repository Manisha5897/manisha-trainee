{
    'name': "My Lunch Box",
    'version': '1.0',
    'depends': ["web", "base"],
    'description': """
    This is my lunch box application
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/service_prov.xml',
        'views/customer.xml',
        'views/product.xml',
        'views/order.xml',
        'report/product_report.xml',
    ],
}
