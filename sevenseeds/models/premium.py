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
