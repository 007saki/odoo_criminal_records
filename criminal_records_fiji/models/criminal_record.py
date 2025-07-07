from odoo import models, fields

class CriminalRecord(models.Model):
    _name = 'criminal.record'
    _description = 'Criminal Record'

    person_id = fields.Many2one('criminal.person', required=True)
    conviction_ids = fields.One2many('criminal.conviction', 'record_id')
    date_opened = fields.Date()
    notes = fields.Text()
