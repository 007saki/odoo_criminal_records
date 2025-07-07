from odoo import models, fields

class Address(models.Model):
    _name = 'criminal.address'
    _description = 'Address'

    person_id = fields.Many2one('criminal.person', required=True)
    street = fields.Char()
    city = fields.Char()
    province = fields.Char()
    country = fields.Char(default='Fiji')
    notes = fields.Text()
