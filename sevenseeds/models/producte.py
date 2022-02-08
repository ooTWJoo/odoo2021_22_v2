from odoo import models, fields, api
import random
import math
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


<<<<<<< HEAD
class product_character_slots(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    character_slots = fields.Integer(default=5)
=======
class product_survivor_slots(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    surviver_slots = fields.Integer(default=5)
>>>>>>> f9b543845fa971bf56339da29b7d486047ac6ad2

class sale_slots(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    slots_purchased = fields.Boolean(default=False)

    def apply_slots(self):
<<<<<<< HEAD
        premium_products = self.order_line.filtered(lambda p: p.product_id.character_slots)
        for p in premium_products:
            self.partner_id.apply_slots(p.product_id.character_slots)
=======
        premium_products = self.order_line.filtered(lambda p: p.product_id.survivor_slots)
        for p in premium_products:
            self.partner_id.apply_slots(p.product_id.survivor_slots)
>>>>>>> f9b543845fa971bf56339da29b7d486047ac6ad2

    def write(self, values):
        super(sale_slots, self).write(values)
        self.apply_slots()

    @api.model
    def create(self, values):
        record = super(sale_slots, self).create(values)
        record.apply_slots()
        return record


