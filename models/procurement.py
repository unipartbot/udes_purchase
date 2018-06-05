# -*- coding: utf-8 -*-

from odoo import api, models, registry


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def check_order_points(self, use_new_cursor=False, company_id=False):
        """  Copy of run_scheduler to only check order points """
        try:
            if use_new_cursor:
                cr = registry(self._cr.dbname).cursor()
                self = self.with_env(self.env(cr=cr))

                self.sudo()._procure_orderpoint_confirm(
                    use_new_cursor=use_new_cursor,
                    company_id=company_id)
            if use_new_cursor:
                self._cr.commit()
        finally:
            if use_new_cursor:
                try:
                    self._cr.close()
                except Exception:
                    pass
        return {}
