from odoo import models
import logging

_logger = logging.getLogger(__name__)

class SignupPartnerCompanySync(models.AbstractModel):
    _inherit = 'res.users'

    def _signup_create_user(self, values):
        user = super()._signup_create_user(values)
        if user.partner_id and user.company_ids:
            user.partner_id.company_ids = [(6, 0, user.company_ids.ids)]
            _logger.info(
                "Signup sync: partner.company_ids set to %s for user %s",
                user.company_ids.ids, user.id
            )
        return user
