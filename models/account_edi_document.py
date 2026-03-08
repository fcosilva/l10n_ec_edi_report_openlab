from odoo import models


class AccountEdiDocument(models.Model):
    _inherit = "account.edi.document"

    def _l10n_ec_tax_value_decimals(self):
        self.ensure_one()
        company = self.move_id.company_id or self.env.company
        document_type = self._l10n_ec_get_document_type()
        version_by_document = {
            "invoice": company.l10n_ec_invoice_version,
            "purchase_liquidation": company.l10n_ec_liquidation_version,
            "credit_note": company.l10n_ec_credit_note_version,
            "debit_note": company.l10n_ec_debit_note_version,
        }
        version = version_by_document.get(document_type) or company.l10n_ec_invoice_version
        return 2 if version == "1.0.0" else 6

    def _l10n_ec_prepare_tax_vals_edi(self, tax_data):
        self.ensure_one()
        tax_vals = super()._l10n_ec_prepare_tax_vals_edi(tax_data)
        tax_amount = tax_data.get("tax_amount_currency", 0.0)
        tax_vals["valor"] = self._l10n_ec_number_format(
            abs(tax_amount), self._l10n_ec_tax_value_decimals()
        )
        return tax_vals
