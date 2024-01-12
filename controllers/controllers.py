# -*- coding: utf-8 -*-
from odoo import http

# class EmailNotificationExtended(http.Controller):
#     @http.route('/email_notification_extended/email_notification_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/email_notification_extended/email_notification_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('email_notification_extended.listing', {
#             'root': '/email_notification_extended/email_notification_extended',
#             'objects': http.request.env['email_notification_extended.email_notification_extended'].search([]),
#         })

#     @http.route('/email_notification_extended/email_notification_extended/objects/<model("email_notification_extended.email_notification_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('email_notification_extended.object', {
#             'object': obj
#         })