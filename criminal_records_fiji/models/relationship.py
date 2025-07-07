from odoo import models, fields

class Relationship(models.Model):
    _name = 'criminal.relationship'
    _description = 'Relationship'

    person_id = fields.Many2one('criminal.person', required=True)
    related_person_id = fields.Many2one('criminal.person', string='Related Person')
    relation_type = fields.Char()
    notes = fields.Text()
