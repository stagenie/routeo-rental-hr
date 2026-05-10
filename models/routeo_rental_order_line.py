from odoo import api, models

INTERNAL_DISCOUNT_RATE = 0.7


class RouteoRentalOrderLine(models.Model):
    _inherit = 'routeo.rental.order.line'

    @api.depends('vehicle_id', 'order_id.is_internal')
    def _compute_daily_price(self):
        super()._compute_daily_price()
        for line in self:
            if line.order_id.is_internal:
                line.daily_price = line.daily_price * INTERNAL_DISCOUNT_RATE
