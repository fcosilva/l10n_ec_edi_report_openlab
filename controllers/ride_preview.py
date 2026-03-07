# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import http
from odoo.http import request


class OpenLabRidePreviewController(http.Controller):
    @http.route("/openlab/ride-preview", type="http", auth="user", methods=["GET"])
    def openlab_ride_preview(self, move_id=None, name=None, **kwargs):
        move = self._get_move(move_id=move_id, name=name)
        if not move:
            return request.not_found()

        report = request.env.ref("account.account_invoices")
        html, _ = report._render_qweb_html(report.report_name, [move.id])
        return request.make_response(html)

    def _get_move(self, move_id=None, name=None):
        AccountMove = request.env["account.move"].sudo()
        if move_id:
            move = AccountMove.browse(int(move_id)).exists()
            return move
        if name:
            return AccountMove.search([("name", "=", name)], limit=1)
        return AccountMove.search(
            [
                ("move_type", "=", "out_invoice"),
                ("state", "=", "posted"),
            ],
            order="invoice_date desc, id desc",
            limit=1,
        )
