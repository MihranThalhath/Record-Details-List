from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def fetch_record_details(self) -> str:
        def create_table_row(cells: list) -> str:
            return (
                "<tr>"
                + "".join(
                    f"<td style='border: 1px solid black;'>{cell}</td>"
                    for cell in cells
                )
                + "</tr>"
            )

        order_lines = [
            create_table_row(
                [
                    line.product_id.name[:50],
                    line.name[:50],
                    str(line.product_uom_qty),
                    str(line.price_unit),
                    str(line.price_subtotal),
                ]
            )
            for line in self.order_line
        ]

        if order_lines:
            header = create_table_row(
                ["Product", "Description", "Quantity", "Unit Price", "Subtotal"]
            )
            order_line_text = (
                "<table class='additional-table' style='width: 100%;'>"
                + header
                + "".join(order_lines)
                + "</table>"
            )
        else:
            order_line_text = "<span>No order line details available.</span>"

        return order_line_text
