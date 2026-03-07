# Ecuador EDI Report OpenLab

Modulo Odoo 17 para personalizar el RIDE de facturas electronicas de Ecuador sobre `l10n_ec_account_edi`.

## Que hace

- Ajusta el layout QWeb del PDF RIDE de factura electronica.
- Permite personalizar encabezado, datos del cliente, detalle, formas de pago, subtotales e informacion adicional.
- Mantiene una copia de respaldo del template estable en:
  - `report/ride_invoice_templates_perfect_backup.xml`
- Incluye una ruta de previsualizacion HTML para iterar el diseno mas rapido:
  - `/openlab/ride-preview?name=Fact%20001-100-000000099`
  - `/openlab/ride-preview?move_id=1703`

## Dependencias

- `l10n_ec_account_edi`

## Archivos principales

- `report/ride_invoice_templates.xml`: template QWeb principal del RIDE.
- `models/account_edi_document.py`: ajustes puntuales al XML EDI.
- `controllers/ride_preview.py`: preview HTML del RIDE.
- `static/src/scss/ride_report.scss`: estilos del reporte.

## Instalacion / actualizacion

Desde la raiz del proyecto:

```bash
docker-compose run --rm web-dev odoo -d openlab-dev -u l10n_ec_edi_report_openlab --workers 0 --stop-after-init
docker-compose run --rm web-dev odoo -d openlab-dev -u l10n_ec_edi_report_openlab --workers 0 --test-enable --test-tags /l10n_ec_edi_report_openlab --stop-after-init
docker-compose restart web-dev
```

## Uso

1. Editar `report/ride_invoice_templates.xml`.
2. Actualizar el modulo.
3. Generar el PDF desde Odoo o usar el preview HTML.

## Licencia

Este modulo se distribuye bajo licencia AGPL-3. Ver `LICENSE`.
