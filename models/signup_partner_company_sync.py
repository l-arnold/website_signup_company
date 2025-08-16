from odoo import models

class SignupPartnerCompanySync(models.AbstractModel):
    _inherit = 'res.users'

    def _signup_create_user(self, values):
        user = super()._signup_create_user(values)
        if user.partner_id and user.company_ids:
            user.partner_id.company_ids = [(6, 0, user.company_ids.ids)]
        return user
