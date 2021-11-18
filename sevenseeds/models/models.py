# -*- coding: utf-8 -*-
import random

from odoo.exceptions import ValidationError
from odoo import models, fields, api

class player(models.Model):
     _name = 'sevenseeds.player'
     _description = 'Players'

     name = fields.Char()
     team = fields.Many2one('sevenseeds.team', ondelete='set null')
     avatar = fields.Image(max_width=200, max_height=200)
     avatar_icon = fields.Image(related='avatar', max_width=50, max_height=50)
     characters = fields.One2many('sevenseeds.character', 'player')
     quantity_characters = fields.Integer(compute='_get_q_characters')

     @api.depends('characters')
     def _get_q_characters(self):
          for p in self:
               p.quantity_characters = len(p.characters)

     def create_character(self):
          for p in self:
               template = random.choice(self.env['sevenseeds.character_template'].search([]).mapped(lambda t: t.id))
               area = random.choice(self.env['area.city'].search([]).mapped(lambda t: t.id))
               self.env['sevenseeds.character'].create({'player': p.id, 'template': template, 'area': area})


class team(models.Model):
     _name = 'sevenseeds.team'
     _description = 'Teams'

     name = fields.Char()
     character = fields.One2many('sevenseeds.player', 'team')

class character(models.Model):
     _name = 'sevenseeds.character'
     _description = 'Character'

     sex = fields.Selection([('male', 'Male'), ('female', 'Female')])

     name = fields.Char()
     mood = fields.Float(default = 70.00)
     illness = fields.Float(default = 1.00)
     player = fields.Many2one('sevenseeds.player', ondelete='set null')
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

     @api.onchange('sex')
     def _get_name(self):
          if self.sex == 'male':
                    first = ["Kenny", "Matt", "Nick", "Adam", "Brandon", "Luke", "Karl", "Micheal", "Tama", "Tanga",
                             "AJ", "Finn", "Jay", "Marty", "Chris", "Sammy", "Jake", "Santana", "Ortiz", "Darby",
                             "Maxwell J.", "Jungle", "Evil", "Stu", "Colt", "John", "Alex", "Ten", "Alan V", "Brodie"]
                    second = ["Omega", "Jackson", "Page", "Cole", "Cutler", "Gallows", "Anderson", "Nakazawa",
                              "Tonga", "Loa", "Styles", "Bálor", "White", "Scurll", "Jericho", "Guevara", "Hager",
                              "Proud", "Powerful", "Allin", "Friedman", "Boy", "Uno", "Grayson", "Cabana", "Silver",
                              "Reynolds", "Ten", "Angels", "Lee", "Smegg"]

                    self.name = random.choice(first) + " " + random.choice(second)
          elif self.sex == 'female':
                    first = ["Kris", "AJ", "Anna", "Jade", "The", "Penelope", "Hikaru", "Ruby", "Charlotte", "Paige",
                               "Julia", "Alexa", "Brandi", "Britt", "Jamie", "Abadon", "Leva", "Leyla", "Nyla", "Serena",
                               "Tay", "Thunder", "Sasha", "Bayley", "Becky", "Nia", "Ember", "Eva", "Torrie", "Stephanie"]
                    second = ["Statlander", "Lee", "Jay", "Cargill", "Bunny", "Ford", "Shida", "Soho", "Flair", "Stars",
                                "Hart", "Bliss", "Rhodes", "Baker", "Hayter", "Mass", "Bates", "Hersch", "Rose", "Deeb",
                                "Conti", "Rosa", "Banks", "Ivelisse", "Lynch", "Jax", "Moon", "Marie", "Wilson", "McMahon"]
                    self.name = random.choice(first) + " " + random.choice(second)

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
     livability = fields.Float(default=50.00)  # %
     happiness = fields.Float(default=50.00)  # %

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
     health = fields.Float(defualt=100.00)
     type = fields.Selection([('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('horse', 'Horse'),
                              ('fox', 'Fox'), ('monkey', 'Monkey')])
     character = fields.Many2one('sevenseeds.character', ondelete='set null')

class base(models.Model):
     _name = 'sevenseeds.base'
     _description = 'Base'

     name = fields.Char()
     level = fields.Float(default=1.00)
     condition = fields.Float(default=50.00) # 0 is new, 100 is bRoKeN
     character = fields.Many2one('sevenseeds.character', ondelete='set null')
     area = fields.Many2one('sevenseeds.area', ondelete='set null')







