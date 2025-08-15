from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

class WebsiteSignupCompany(AuthSignupHome):

    def _get_allowed_companies(self, user):
        """Return the list of company IDs the user is allowed to access."""
        return user.company_ids.ids if user else []

    def do_signup(self, qcontext):
        user = super().do_signup(qcontext)
        website_company = request.website.company_id

        if user and website_company:
            user = user.sudo()
            allowed_company_ids = self._get_allowed_companies(user)

            user.write({
                'company_id': website_company.id,
                'company_ids': [(6, 0, allowed_company_ids)]
            })

            partner = user.partner_id.sudo()
            if partner:
                partner.write({
                    'company_id': website_company.id,
                    'company_ids': [(6, 0, allowed_company_ids)]
                })

        return user
