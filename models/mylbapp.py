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
    image = fields.Binary(string='Food Image')
    product_type = fields.Selection([
        ('Half', 'Half'),
        ('Full', 'Full'),
    ], string='Food Type')
    price = fields.Integer(string='Price')

class Order(models.Model):
    _name = 'order.food.order'
    _description = 'food order detail'

    name = fields.Many2one('customer.detail', string='Customer Name')
    # name = fields.Char(string='Customer Name')
    food_name = fields.Many2one('product.data.product', string='Food Name')
    food_provider_name = fields.Many2one('meal.provider.detail', string='Food Provider Name')
    order_date = fields.Datetime(string='Order Date & Time')
    delivery_type = fields.Selection([
        ('Home Delivery', 'Home Delivery'),
        ('Own Delivery', 'Own Delivery'),
        ], string='Delivery Type', required=True)
    state = fields.Selection([('draft', 'Draft'), ('pending', 'Pending'), ('cancel', 'Cancel'), ('done', 'Done')], default='')

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_pending(self):
        self.write({'state': 'pending'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_done(self):
        self.write({'state': 'done'})
