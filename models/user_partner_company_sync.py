from odoo import models

class UserPartnerCompanySync(models.Model):
    _inherit = 'res.users'

    def write(self, vals):
        res = super().write(vals)
        if 'company_ids' in vals:
            for user in self:
                if user.partner_id:
                    user.partner_id.company_ids = [(6, 0, user.company_ids.ids)]
        return res
