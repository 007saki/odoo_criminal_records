from odoo import models, fields

class Person(models.Model):
    _name = 'criminal.person'
    _description = 'Person'

    name = fields.Char(required=True)
    date_of_birth = fields.Date()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    national_id = fields.Char()
    address_ids = fields.One2many('criminal.address', 'person_id')
    fingerprint_ids = fields.One2many('criminal.fingerprint', 'person_id')
    relationship_ids = fields.One2many('criminal.relationship', 'person_id')
    criminal_record_ids = fields.One2many('criminal.record', 'person_id')
