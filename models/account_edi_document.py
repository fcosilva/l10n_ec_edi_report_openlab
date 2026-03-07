from odoo import models


class AccountEdiDocument(models.Model):
    _inherit = "account.edi.document"

    def _l10n_ec_prepare_tax_vals_edi(self, tax_data):
        tax_vals = super()._l10n_ec_prepare_tax_vals_edi(tax_data)
        tax_amount = tax_data.get("tax_amount_currency", 0.0)
        tax_vals["valor"] = self._l10n_ec_number_format(abs(tax_amount), 2)
        return tax_vals
