from odoo import http
from odoo.http import request

class CustomAuthSignup(http.Controller):

    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        response = super(CustomAuthSignup, self).web_auth_signup(*args, **kw)

        # After signup, get the new user
        login = kw.get('login')
        user = request.env['res.users'].sudo().search([('login', '=', login)], limit=1)
        website_company = request.website.company_id

        if user:
            # Assign default and allowed companies
            user.sudo().write({
                'company_id': website_company.id,
                'company_ids': [(6, 0, request.env['res.company'].sudo().search([]).ids)]
            })

            # Assign partner company
            if user.partner_id:
                user.partner_id.sudo().write({
                    'company_id': website_company.id
                })

        return response
