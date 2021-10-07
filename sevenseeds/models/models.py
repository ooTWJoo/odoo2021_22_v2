# -*- coding: utf-8 -*-

from odoo import models, fields, api

class player(models.Model):
     _name = 'sevenseeds.player'
     _description = 'Players'

     name = fields.Char()

class team(models.Model):
     _name = 'sevenseeds.team'
     _description = 'Teams'

     name = fields.Char()




