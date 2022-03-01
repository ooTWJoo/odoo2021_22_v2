# -*- coding: utf-8 -*-
import random
import math

from odoo.exceptions import ValidationError
from odoo import models, fields, api
from datetime import timedelta, datetime

class player(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'


     #name = fields.Char()
     is_player = fields.Boolean(default=False)
     team = fields.Many2one('sevenseeds.team', ondelete='set null')
     avatar = fields.Image(max_width=200, max_height=200)
     avatar_icon = fields.Image(related='avatar', max_width=50, max_height=50)
     characters = fields.One2many('sevenseeds.character', 'player')
     quantity_characters = fields.Integer(compute='_get_q_characters')
     login = fields.Char()
     password = fields.Char()
     max_characters = fields.Integer(default=5)
     medicine_points = fields.Integer(default=100)

     @api.depends('characters')
     def _get_q_characters(self):
          for p in self:
               p.quantity_characters = len(p.characters)

     def apply_slots(self, addslots):
         for p in self:
             p.max_characters = p.max_characters + addslots

     def create_character(self):
          for p in self:
               sex = random.choice(['male', 'female'])
               if sex == 'male':
                    first = ["Kenny", "Matt", "Nick", "Adam", "Brandon", "Luke", "Karl", "Micheal", "Tama", "Tanga",
                             "AJ", "Finn", "Jay", "Marty", "Chris", "Sammy", "Jake", "Santana", "Ortiz", "Darby",
                             "Maxwell Jakob", "Jungle", "Evil", "Stu", "Colt", "John", "Alex", "Ten", "Alan V", "Brodie"]
                    second = ["Omega", "Jackson", "Page", "Cole", "Cutler", "Gallows", "Anderson", "Nakazawa",
                              "Tonga", "Loa", "Styles", "Bálor", "White", "Scurll", "Jericho", "Guevara", "Hager",
                              "Proud", "Powerful", "Allin", "Friedman", "Boy", "Uno", "Grayson", "Cabana", "Silver",
                              "Reynolds", "Ten", "Angels", "Lee", "Smegg"]

                    name = random.choice(first) + " " + random.choice(second)
                    template = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
               elif sex == 'female':
                    first = ["Kris", "AJ", "Anna", "Jade", "The", "Penelope", "Hikaru", "Ruby", "Charlotte", "Paige",
                             "Julia", "Alexa", "Brandi", "Britt", "Jamie", "Abadon", "Leva", "Leyla", "Nyla", "Serena",
                             "Tay", "Thunder", "Sasha", "Bayley", "Becky", "Nia", "Ember", "Eva", "Torrie", "Stephanie"]
                    second = ["Statlander", "Lee", "Jay", "Cargill", "Bunny", "Ford", "Shida", "Soho", "Flair", "Stars",
                              "Hart", "Bliss", "Rhodes", "Baker", "Hayter", "Mass", "Bates", "Hersch", "Rose", "Deeb",
                              "Conti", "Rosa", "Banks", "Ivelisse", "Lynch", "Jax", "Moon", "Marie", "Wilson",
                              "McMahon"]
                    name = random.choice(first) + " " + random.choice(second)
                    template = random.choice(['11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])

               area = random.choice(self.env['sevenseeds.area'].search([]).mapped(lambda t: t.id))
               self.env['sevenseeds.character'].create({'player': p.id, 'sex': sex, 'name': name, 'template': template, 'area': area})




class team(models.Model):
     _name = 'sevenseeds.team'
     _description = 'Teams'

     name = fields.Char()
     character = fields.One2many('res.partner', 'team')

class character(models.Model):
     _name = 'sevenseeds.character'
     _description = 'Character'

     sex = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)

     def _generate_illness(self):
          return round((random.random())*100)

     name = fields.Char()
     mood = fields.Float(default = 70.00)
     illness = fields.Float(default = _generate_illness)
     player = fields.Many2one('res.partner', ondelete='set null')
     area = fields.Many2one('sevenseeds.area', ondelete='restrict')
     job = fields.Many2one('sevenseeds.job', ondelete='set null')
     weapon = fields.Many2one('sevenseeds.weapon', ondelete='set null')
     skill = fields.Many2many(comodel_name='sevenseeds.skill')
     base = fields.One2many('sevenseeds.base', 'character')
     pet = fields.One2many('sevenseeds.pet', 'character')
     template = fields.Many2one('sevenseeds.character_template', ondelete='restrict')
     avatar = fields.Image(max_width=200, max_height=400, related='template.image')
     state = fields.Selection(string="state", selection=[('draft', 'Draft'), ('confirm', 'Confirmed')], required=False, default="draft")

     def btn_draft(self):
          self.state = "draft"

     def btn_confirm(self):
          self.state = "confirm"

     def btn_heal(self):
         for c in self:
             if c.illness > 0:
                 c.illness = 0
             if c.player.medicine_points > 9:
                 c.player.medicine_points - 10
                 c.illness = 0
             else:
                 raise ValidationError("Not enough Medicine Points")

     @api.constrains('player')
     def _check_quantity_characters(self):
         for character in self:
             print(character.player.max_characters, character.player.quantity_characters)
             if character.player.quantity_characters > character.player.max_characters:
                raise ValidationError("Max " + str(character.player.max_characters) + " characters. Purchase more character slots to create another character.")

     @api.constrains('skill')
     def _check_skill_count(self):
          for character in self:
               if len(character.skill) > 3:
                    raise ValidationError("Max 3 Skills")

     @api.onchange('sex')
     def _get_name(self):
          if self.sex == 'male':
                    first = ["Kenny", "Matt", "Nick", "Adam", "Brandon", "Luke", "Karl", "Micheal", "Tama", "Tanga",
                             "AJ", "Finn", "Jay", "Marty", "Chris", "Sammy", "Jake", "Santana", "Ortiz", "Darby",
                             "Maxwell Jakob", "Jungle", "Evil", "Stu", "Colt", "John", "Alex", "Ten", "Alan V", "Brodie"]
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

     def _generate_position(self):
        existent_areas = self.search([])
        x = random.randint(-100, 100)
        for e in existent_areas:
            if e.position_x != x:
                return x

     name = fields.Char()
     energy = fields.Float()
     food = fields.Float()
     water = fields.Float()
     livability = fields.Float(default=50.00)  # %
     happiness = fields.Float(default=50.00)# %
     routes = fields.Many2many("sevenseeds.route", compute='_get_routes')
     character = fields.One2many('sevenseeds.character', 'area')
     base = fields.One2many('sevenseeds.base', 'area')
     position_x = fields.Integer(default=_generate_position)
     position_y = fields.Integer(default=_generate_position)

     def _get_routes(self):
         for a in self:
             a.routes=self.env['sevenseeds.route'].search(['|', ('area_1', '=', a.id), ('area_2', '=', a.id)]).ids

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
     health = fields.Float(default=99.00)
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

class route(models.Model):
    _name = 'sevenseeds.route'
    _description = 'Route'

    name = fields.Char(compute='_set_name')
    area_1 = fields.Many2one('sevenseeds.area', ondelete='cascade')
    area_2 = fields.Many2one('sevenseeds.area', ondelete='cascade')
    distance = fields.Float(compute='_generate_distance')

    @api.depends('area_1', 'area_2')
    def _generate_distance(self):
        for r in self:
            r.distance = math.sqrt((r.area_1.position_x - r.area_1.position_x)** 2 + (r.area_2.position_x - r.area_2.position_y)** 2)

    @api.onchange('distance')
    def _set_name(self):
        for r in self:
            r.name = r.area_1.name, " ---- ", r.area_2.name

class journey(models.Model):
    _name = 'sevenseeds.journey'
    _description = 'Journey'

    name = fields.Char(default='Journey')
    origin = fields.Many2one('sevenseeds.area', ondelete='cascade')
    destination = fields.Many2one('sevenseeds.area', ondelete='cascade')
    routes = fields.Many2one('sevenseeds.route', ondelete='cascade')
    date_start = fields.Datetime(default=lambda r: fields.datetime.now())
    date_finish = fields.Datetime(compute='_get_status')
    status = fields.Float(compute='_get_status')
    state = fields.Selection([('preparing', 'Preparing'), ('inprogress', 'In Progress'), ('finished', 'Finished')],
                             default='preparing')

    player = fields.Many2one('res.partner')
    passengers = fields.Many2many('sevenseeds.character')

    @api.onchange('destination')
    def _onchange_destination(self):
        if self.destination != False:
            routes_available = self.origin.routes & self.destination.routes
            self.routes = routes_available.id
            return {}

    def launch_travel(self):
        for j in self:
            j.date_start = fields.datetime.now()
            j.state = 'inprogress'
            for p in j.passengers:
                p.area = False

    @api.depends('date_start', 'routes')
    def _get_status(self):
        for j in self:
            if j.routes:
                print(j.routes.distance)
                if j.date_start:
                    d_start = j.date_start
                    date = fields.Datetime.from_string(d_start)
                    date = date + timedelta(hours=j.routes.distance)
                    j.date_finish = fields.Datetime.to_string(date)
                    time_left = fields.Datetime.context_timestamp(self, j.date_finish)-fields.Datetime.context_timestamp(self, datetime.now())
                    time_left = time_left.total_seconds() / 60 / 60
                    j.status = (1 - time_left / j.routes.distance) * 100
                    if j.status >= 100:
                        j.status = 100
                else:
                    j.status = 0;
                    j.date_finish = False
            else:
                j.status = 0
                j.date_finish = False

    @api.model
    def update_travel(self):
        journeys_in_progress = self.search([('state', '=', 'inprogress')])
        print("Updating progress in: ", journeys_in_progress)
        for j in journeys_in_progress:
            if j.status >= 100:
                j.write({'state': 'finished'})
                for p in j.passengers:
                    p.write({'area': j.destination.id})
                self.env['sevenseeds.event'].create(
                    {'name': 'Journey arrival ' + j.name, 'player': j.player, 'event': 'sevenseeds.journey,' + str(j.id), 'description': 'Journey arrival... '})
                print('Arrival')


class event(models.Model):
    _name = 'sevenseeds.event'
    _description = 'Events'

    name = fields.Char()
    player = fields.Many2many('res.partner')
    event = fields.Reference([('sevenseeds.journey', 'Journey')])
    description = fields.Text()

class wizard_pet(models.TransientModel):
    _name = 'sevenseeds.wizard_pet'

    def next(self):
        if self.state=='1':
            self.state='2'
        elif self.state=='2':
            self.state='3'
        return {'type': 'ir.actions.act_window',
                'res_model': self._name,
                'res_id': self.id,
                'view_mode': 'form',
                'target': 'new',
                }
    def previous(self):
        if (self.state=='3'):
            self.state='2'
        elif (self.state=='2'):
            self.state='1'
        return {'type': 'ir.actions.act_window',
                'res_model': self._name,
                'res_id': self.id,
                'view_mode': 'form',
                'target': 'new',
                }

    name = fields.Char()
    type = fields.Selection([('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('horse', 'Horse'),
                             ('fox', 'Fox'), ('monkey', 'Monkey')])
    character = fields.Many2one('sevenseeds.character')
    state = fields.Selection([('1', 'name'), ('2', 'type'), ('3', 'character')], default='1')

    def btn_createpet(self):
        pet = self.env['sevenseeds.pet'].create({'name': self.name, 'type': self.type, 'character': self.character.id})


class wizard_medicine(models.TransientModel):


    def _getPlayer(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))

    def _getSick(self):
        sickPeeps = self.env['res.partner'].browse(self._context.get('active_id')).characters
        sickPeeps = sickPeeps.filtered(lambda i: i.illness > 0).ids
        return sickPeeps



    _name = 'sevenseeds.wizard_medicine'

    player = fields.Many2one('res.partner', default=_getPlayer)
    sickPeeps = fields.Many2many('sevenseeds.character', default=_getSick)
    medicine_points = fields.Integer(related='player.medicine_points')




















