# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class player(models.Model):
     _name = 'sevenseeds.player'
     _description = 'Players'

     name = fields.Char()
     avatar = fields.Image(max_width=200, max_height=200)
     avatar_icon = fields.Image(related='avatar', max_width=50, max_height=50)
     character = fields.One2many('sevenseeds.character', 'player')


class team(models.Model):
     _name = 'sevenseeds.team'
     _description = 'Teams'

     name = fields.Char()
     character = fields.One2many('sevenseeds.character', 'area')

class character(models.Model):
     _name = 'sevenseeds.character'
     _description = 'Character'

     name = fields.Char()
     player = fields.Many2one('sevenseeds.player', ondelete='set null')
     team = fields.Many2one('sevenseeds.team', ondelete='set null')
     area = fields.Many2one('sevenseeds.area', ondelete='restrict')
     job = fields.Many2one('sevenseeds.job', ondelete='set null')
     weapon = fields.Many2one('sevenseeds.weapon', ondelete='set null')
     skill = fields.Many2many(comodel_name='sevenseeds.skill')
     base = fields.One2many('sevenseeds.base', 'character')
     pet = fields.One2many('sevenseeds.pet', 'character')
     template = fields.Many2one('sevenseeds.character_template', ondelete='restrict')
     avatar = fields.Image(max_width=200, max_height=400, related='template.image')

     @api.constrains('skill')
     def _check_something(self):
          for character in self:
               if len(character.skill) > 3:
                    raise ValidationError("Max 3 Skills")

class character_template(models.Model):
    _name = 'sevenseeds.character_template'
    _description = 'Templates to generate characters'

    name = fields.Char()
    image = fields.Image(max_width=200, max_height=400)

class area(models.Model):
     _name = 'sevenseeds.area'
     _description = 'Area'

     name = fields.Char()
     energy = fields.Float()
     food = fields.Float()
     water = fields.Float()
     livability = fields.Float(default=50)  # %
     happiness = fields.Float(default=50)  # %

     character = fields.One2many('sevenseeds.character', 'area')
     base = fields.One2many('sevenseeds.base', 'area')

class skill(models.Model):
     _name = 'sevenseeds.skill'
     _description = 'Skills'

     name = fields.Char()
     character = fields.Many2many(comodel_name='sevenseeds.character')

class job(models.Model):
     _name = 'sevenseeds.job'
     _description = 'Job'

     name = fields.Char()
     character = fields.One2many('sevenseeds.character', 'job')

class weapon(models.Model):
     _name = 'sevenseeds.weapon'
     _description = 'Weapon'

     name = fields.Char()
     character = fields.One2many('sevenseeds.character', 'weapon')

class pet(models.Model):
     _name = 'sevenseeds.pet'
     _description = 'Pet'

     name = fields.Char()
     character = fields.Many2one('sevenseeds.character', ondelete='set null')

class base(models.Model):
     _name = 'sevenseeds.base'
     _description = 'Base'

     name = fields.Char()
     character = fields.Many2one('sevenseeds.character', ondelete='set null')
     area = fields.Many2one('sevenseeds.area', ondelete='set null')






