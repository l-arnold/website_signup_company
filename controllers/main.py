from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class WebsiteSignupCompany(AuthSignupHome):

    def do_signup(self, qcontext):
        user = super().do_signup(qcontext)
        website_company = request.website.company_id

        if user and website_company:
            user = user.sudo()
            user.write({
                'company_id': website_company.id,
                'company_ids': [(6, 0, [website_company.id])]
            })
            if user.partner_id:
                user.partner_id.sudo().write({
                    'company_id': website_company.id
                })
        return user