from odoo import api, fields, models


class RouteoRentalOrder(models.Model):
    _inherit = 'routeo.rental.order'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employé',
        ondelete='restrict',
    )
    is_internal = fields.Boolean(
        string='Location interne',
        compute='_compute_is_internal',
        store=True,
    )

    @api.depends('employee_id')
    def _compute_is_internal(self):
        for order in self:
            order.is_internal = bool(order.employee_id)
