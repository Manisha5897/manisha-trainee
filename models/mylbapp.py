from odoo import api, fields, models

class MealProvider(models.Model):
    _name = 'meal.provider.detail'
    _description = 'meal provider detail'

    product_id = fields.Many2many('product.data.product',string='Product Id')
    name = fields.Char(string='Owner Name', help='Meal Provider Name')
    company_name = fields.Char(string='Food Company Name')
    specialist = fields.Char(string='Specialist in Food')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')
    terms_and_condition = fields.Text(string='Terms & Conditions')

class Customer(models.Model):
    _name = 'customer.detail'
    _description = 'customer details'

    name = fields.Char(string='Customer Name')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

class Product(models.Model):
    _name = 'product.data.product'
    _description = 'product details'

    name = fields.Char(string='Product Name')
    product_type = fields.Selection([
        ('half', 'Half'),
        ('full', 'Full'),
    ], string='Product Type')
    price = fields.Integer(string='Product Price')