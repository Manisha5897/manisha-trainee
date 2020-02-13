from odoo import fields, models


class Customer(models.TransientModel):
    _name = 'customer.customer.details'
    _description = 'Customer detail'

    name = fields.Char(string='Customer Name')
    address = fields.Text(string='Address')
    contact = fields.Integer(string='Contact No')
    email = fields.Char(string='E-mail')

    def data_save(self):
        self.env['customer.detail'].create({
            'name': self.name,
            'address': self.address,
            'contact': self.contact,
            'email': self.email,
            })
