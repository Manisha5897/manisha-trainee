from odoo import api, fields, models

class MealProvider(models.Model):
    _name = 'meal.provider.detail'
    _description = 'meal provider detail'

    product_id = fields.Many2many('product.data.product',string='Food Id')
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

# Food
class Product(models.Model):
    _name = 'product.data.product'
    _description = 'product details'

    name = fields.Char(string='Food Name')
    product_type = fields.Selection([
        ('Half', 'Half'),
        ('Full', 'Full'),
    ], string='Food Type')
    price = fields.Integer(string='Price')

# class Order(models.Model):
#     _name = 'order.food.order'
#     _description = 'food order detail'

#     meal_provider_name
#     company_name
#     address
#     contact
#     food_id->name foodtype price
#     customer_name
#     address
#     contact
#     order date & time
#     delivery->yes/no yes->delivery charge
#     status