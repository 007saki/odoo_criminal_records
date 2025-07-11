from odoo import models, fields

class Fingerprint(models.Model):
    _name = 'criminal.fingerprint'
    _description = 'Fingerprint'

    person_id = fields.Many2one('criminal.person', required=True)
    image = fields.Binary('Fingerprint Image')
    date_taken = fields.Date()
    notes = fields.Text()