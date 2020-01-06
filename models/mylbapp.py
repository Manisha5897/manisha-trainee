from odoo import api, fields, models

class ServiceProv(models.Model):
    _name = 'service.provider.detail'
    _description = 'service provider details'

    # providerid = fields.Many2one('source.model.name', string='Provider Id')
    provnm = fields.Char(string='Service Provider Name')
    # password = 
    specialist = fields.Char(string='Specialist in Food')
    prodttype = fields.Selection([
        ('half', 'Half'),
        ('full', 'Full'),
        ('both', 'Both'),
    ], string='Product Type')
    proddprice = fields.Integer(string='Product Price')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

class Customer(models.Model):
    _name = 'customer.detail'
    _description = 'customer details'

    # custid = fields.Many2one('source.model.name', string='Customer Id')
    custnm = fields.Char(string='Customer Name')
    # password = 
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

class Product(models.Model):
    _name = 'product.product'
    _description = 'product details'
    _rec_name = 'prodnm'
    # _inherit = 'order.prod.order'

    # prodid = fields.Many2one('source.model.name', string='Product Id')
    prodnm = fields.Char(string='Product Name')
    prodtype = fields.Selection([
        ('half', 'Half'),
        ('full', 'Full'),
        ('both', 'Both'),
    ], string='Product Type')
    prodprice = fields.Integer(string='Product Price')

class Order(models.Model):
    _name = 'order.prod.order'
    _description = 'order details'

    prodordernm = fields.Many2many('product.product', string='Order Product Name')
    # orderid = fields.Many2one('source.model.name', string='Order Id')
    # inherited fields....................
    # prodnm = fields.Char(string='Product Name')
    # prodtype = fields.Selection([
    #     ('half', 'Half'),
    #     ('full', 'Full'),
    # ], string='Product Type')
    # prodprice = fields.Integer(string='Product Price')

# class Service(models.Model):
#     _name = 'service.delivery.service'
#     _description = 'MyLunchBox'

#     # serviceid = fields.Many2one('source.model.name', string='Service Id')
#     # deliveryservice = [radio btn] home or own
#     deliservcharge = fields.Integer(string='Delivery Service Charge')
#     # service on/off

# class Payment(models.Model):
#     _name = 'product.payment'
#     _description = 'MyLunchBox'

#     # payid = 
#     # providerid = 
#     # custid = 
#     # prodid = or orderid
#     # serviceid