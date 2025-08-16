from odoo import models
import logging

_logger = logging.getLogger(__name__)

class UserPartnerCompanySync(models.Model):
    _inherit = 'res.users'

    def write(self, vals):
        res = super().write(vals)
        if 'company_ids' in vals:
            for user in self:
                if user.partner_id:
                    user.partner_id.company_ids = [(6, 0, user.company_ids.ids)]
                    _logger.info(
                        "Update sync: partner.company_ids updated to %s for user %s",
                        user.company_ids.ids, user.id
                    )
        return res
