from odoo import http

class Mylb(http.Controller):
    @http.route('/mylb/mylb/', auth='public', website=True)
    def index(self, **kw):
        data = http.request.env['mylb.data']
        return http.request.render('mylb.index', {
        	'data': data.search([])
        	})