from odoo import models, fields

class Conviction(models.Model):
    _name = 'criminal.conviction'
    _description = 'Conviction'

    # Fix: use Many2one, not 'in'
    record_id = fields.Many2one('criminal.record', required=True)
    conviction_date = fields.Date()
    offense = fields.Char()
    sentence = fields.Char()
    notes = fields.Text()
