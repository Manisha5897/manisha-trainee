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
            return '/my/index/'
        return super(DataShow, self)._login_redirect(uid, redirect=redirect)

class DataShow(Controller):
    @http.route('/my/index/', auth='public', type="http", csrf=False)
    def index(self, **kw):
        data = request.env['product.data.product'].sudo().search([])
        return request.render("manisha_trainee_lunchbox.food_template", {'data': data})

class PortalAccount(CustomerPortal):
    @http.route('/company_register/', auth='public', type='http', csrf=False, website=True)
    def manager_form(self, **kw):
        if request.httprequest.method == 'POST':
            if request.params.get('optradio') == '8':
                request.env['res.users'].sudo().create({
                    'name': request.params.get('username'),
                    'login': request.params.get('username'),
                    'password': request.params.get('password'),
                    'groups_id': [(6, 0, [request.env.ref('base.group_portal').id])],
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

            if request.params.get('optradio') == '1':
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

    # @http.route('/user_register/', auth='public', type='http', csrf=False, website=True)
    # def user_form(self, **kw):
    #     if request.httprequest.method == 'POST':
    #         if request.params.get('optradio') == '8':
    #             request.env['res.users'].sudo().create({
    #                 'name': request.params.get('username'),
    #                 'login': request.params.get('username'),
    #                 'password': request.params.get('password'),
    #                 'groups_id': [(6, 0, [request.env.ref('base.group_portal').id])],
    #             })

    #         return request.redirect('/web/login')

    #     # record = request.env['customer.detail'].sudo().search([])
    #     return request.render('manisha_trainee_lunchbox.user_register')