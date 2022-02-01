from odoo import models, fields, api
import random
import math
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class player_premium(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_premium = fields.Boolean()
    date_end = fields.Datetime()


class product_premium(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    is_premium = fields.Boolean(default=False)

    max_characters = fields.Integer()

class sale_premium(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    premium_applied = fields.Boolean(default=False)

    def apply_premium(self):
        premium_products = self.order_line.filtered(
            lambda p: p.product_id.is_premium == True and self.premium_applied == False)
        for p in premium_products:
            self.partner_id.apply_premium(p.product_id.days_premium)
        self.premium_applied = True

    def write(self, values):
        super(sale_premium, self).write(values)
        self.apply_premium()

    @api.model
    def create(self, values):
        record = super(sale_premium, self).create(values)
        record.apply_premium()
        return 

