# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hr_expense_sheet(models.Model):
    _inherit = 'hr.expense.sheet'

    user_id = fields.Many2one('res.users', string='Approving Manager', required=True)
    url = fields.Char('Url')

    # Notify manager of expense submitted.
    @api.multi
    def send_email_template(self):
        model_id = self.env['hr.expense.sheet']
        form = self.env.ref('hr_expense.view_hr_expense_sheet_form')
        action_id = self.env.ref('hr_expense.action_hr_expense_sheet_my_all')
        self.url = '/web#id=' + str(self.id) + '&view_type=form&model=hr.expense&action=' + str(action_id.id)

        rendering_context = dict(self._context)
        rendering_context.update({
            'action_id': self.env.ref('hr_expense.action_hr_expense_sheet_my_all').id,
            'dbname': self._cr.dbname,
            'base_url': self.env['ir.config_parameter'].get_param('web.base.url', default='http://localhost:8069')
        })

        template = self.env.ref('email_notification_extended.expense_email_template')
        self.env['mail.template'].browse(template.id).with_context(rendering_context).send_mail(self.id, force_send=True)

        return True

    # Remind expense owner to attach receipt

    @api.multi
    def send_reminder_email_template(self):
        model_id = self.env['hr.expense.sheet']
        form = self.env.ref('hr_expense.view_hr_expense_sheet_form')
        action_id = self.env.ref('hr_expense.action_hr_expense_sheet_my_all')
        self.url = '/web#id=' + str(self.id) + '&view_type=form&model=hr.expense&action=' + str(action_id.id)

        rendering_context = dict(self._context)
        rendering_context.update({
            'action_id': self.env.ref('hr_expense.action_hr_expense_sheet_my_all').id,
            'dbname': self._cr.dbname,
            'base_url': self.env['ir.config_parameter'].get_param('web.base.url', default='http://localhost:8069')
        })

        template = self.env.ref('email_notification_extended.attach_receipt_email_template')
        self.env['mail.template'].browse(template.id).with_context(rendering_context).send_mail(self.id, force_send=True)
        
        return True
