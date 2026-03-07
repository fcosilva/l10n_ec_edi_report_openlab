{
    "name": "Ecuador EDI Report OpenLab",
    "version": "17.0.1.0.0",
    "summary": "Improves the visual layout of Ecuadorian electronic invoice PDFs",
    "author": "OpenLab Ecuador",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": ["l10n_ec_account_edi"],
    "data": [
        "report/ride_invoice_templates.xml",
    ],
    "assets": {
        "web.report_assets_common": [
            "l10n_ec_edi_report_openlab/static/src/scss/ride_report.scss",
        ],
    },
    "installable": True,
    "application": False,
}
