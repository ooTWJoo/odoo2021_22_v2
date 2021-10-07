# -*- coding: utf-8 -*-
from odoo import http
import json
# from odoo import tools

class banner_controller_sevenseeds(http.Controller):
    @http.route('/sevenseeds/banner', auth = 'user', type='json')
    def banner(self):
        return{
            'html': """
            <div class="sevenseeds_banner" style="height: 200px; background-size: 100%; background-image: url(/sevenseeds/static/src/img/sevenSeeds.png)">
            """
        }
# class Sevenseeds(http.Controller):
#     @http.route('/sevenseeds/sevenseeds/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sevenseeds/sevenseeds/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sevenseeds.listing', {
#             'root': '/sevenseeds/sevenseeds',
#             'objects': http.request.env['sevenseeds.sevenseeds'].search([]),
#         })

#     @http.route('/sevenseeds/sevenseeds/objects/<model("sevenseeds.sevenseeds"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sevenseeds.object', {
#             'object': obj
#         })
