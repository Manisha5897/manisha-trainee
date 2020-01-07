from odoo import api, fields, models
from datetime import datetime

class ServiceProv(models.Model):
    _name = 'service.provider.detail'
    _description = 'service provider details'

    # providerid = fields.Many2one('source.model.name', string='Provider Id')
    provnm = fields.Char(string='Service Provider Name')
    specialist = fields.Char(string='Specialist in Food')
    prodttype = fields.Selection([
        ('half', 'Half'),
        ('full', 'Full'),
        ('both', 'Both'),
    ], string='Product Type')
    proddprice = fields.Integer(string='Product Price')
    # specialist = fields.Many2one('product.data.product',string='Specialist in Food')
    # prodttype = fields.Many2one('product.data.product',string='Product Type')
    # proddprice = fields.Many2one('product.data.product',string='Product Price')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

class Customer(models.Model):
    _name = 'customer.detail'
    _description = 'customer details'

    # custid = fields.Many2one('source.model.name', string='Customer Id')
    custnm = fields.Char(string='Customer Name')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

class Product(models.Model):
    _name = 'product.data.product'
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
    state = fields.Selection([('draft', 'New'), ('confirm', 'Confirm'), ('done', 'Done')], default='draft')
    product_start_date = fields.Date(string='Product Enter Date', default=str(datetime.today()))
    product_end_date = fields.Date(string='Product End Date', default=str(datetime.today()))
    total_day = fields.Integer(string='Total Service of Day', compute="compute_total")

    def compute_total(self):
        for i in self:
            if i.product_start_date and i.product_end_date:
                diff = i.product_end_date - i.product_start_date
                i.total_day = diff.days
            else:
                i.total_day = 2

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

class Order(models.Model):
    _name = 'order.prod.order'
    _description = 'order details'

    prodordernm = fields.Many2many(
        'product.data.product', string='Order Product Name')
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