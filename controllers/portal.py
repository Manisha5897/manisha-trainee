# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request, Controller
from odoo.addons.web.controllers.main import Home
from odoo.addons.portal.controllers.portal import CustomerPortal


class Home(Home):
    def _login_redirect(self, uid, redirect=None):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('manisha_trainee_lunchbox.group_manager'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_portal'):
            return '/index/'
        return super(DataShow, self)._login_redirect(uid, redirect=redirect)


class DataShow(Controller):
    @http.route('/index/', auth='public', type="http", csrf=False)
    def index(self, **kw):
        data = request.env['product.data.product'].sudo().search([])
        meal = request.env['meal.provider.detail'].sudo().search([])
        return request.render("manisha_trainee_lunchbox.food_template", {'data': data, 'meal': meal})

    @http.route(['/orderfood/<int:m_id>'], auth='public', type="http", csrf=False)
    def orderfood(self, m_id=None, **kw):
        meal = request.env['meal.provider.detail'].sudo()
        if m_id:
            # data = request.env['product.data.product'].sudo().browse([m_id])
            meal = meal.browse([m_id])
        return request.render("manisha_trainee_lunchbox.order_template", {'meal': meal})

    @http.route(['/order/<int:m_id>/<int:p_id>/'], auth='public', type='http', csrf=False)
    def order(self, m_id=None, p_id=None, **kw):
        if not request.session.uid:
            return http.local_redirect('/company_register/')

        if m_id and p_id:
            meal_provider = request.env['meal.provider.detail'].sudo().browse([
                m_id])
            product_data = request.env['product.data.product'].sudo().browse([p_id])
        return request.render("manisha_trainee_lunchbox.myorder_template", {"mp": meal_provider,
                                                                            "pd": product_data})


class PortalAccount(CustomerPortal):
    @http.route('/company_register/', auth='public', type='http', csrf=False, website=True)
    def manager_form(self, **kw):
        if request.httprequest.method == 'POST':
            if request.params.get('optradio') == '8':
                request.env['customer.detail'].sudo().create({
                    'name': request.params.get('username'),
                    'email': request.params.get('email'),
                    'password': request.params.get('password'),
                    'contact': request.params.get('contactno'),
                    'address': request.params.get('address'),
                })

            if request.params.get('optradio') == '1':
                partner = request.env['res.partner'].sudo().create({
                    'name': request.params.get('username'),
                    'email': request.params.get('username'),
                })

                currency = request.env['res.company'].browse(
                    request.params.get('currency_id'))

                company = request.env['res.company'].sudo().create({
                    'name': request.params.get('companyname'),
                    'currency_id': currency.id,
                    'partner_id': partner.id,
                })

                request.env['res.users'].sudo().create({
                    'login': request.params.get('username'),
                    'password': request.params.get('password'),
                    'name': request.params.get('username'),
                    'company_id': company.id,
                    'company_ids': [(4, company.id)],
                    'groups_id': [(6, 0, [request.env.ref('manisha_trainee_lunchbox.group_manager').id])],
                })

            return request.redirect('/web/login')
        data = request.env['res.currency'].sudo().search([])
        return request.render('manisha_trainee_lunchbox.company_register', {"data": data})
