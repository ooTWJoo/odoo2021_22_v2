# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectHome(http.Controller):
#     @http.route('/project_home/project_home/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_home/project_home/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_home.listing', {
#             'root': '/project_home/project_home',
#             'objects': http.request.env['project_home.project_home'].search([]),
#         })

#     @http.route('/project_home/project_home/objects/<model("project_home.project_home"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_home.object', {
#             'object': obj
#         })
