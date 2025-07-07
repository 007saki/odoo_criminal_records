{
    'name': 'Criminal Records Fiji',
    'version': '1.0',
    'summary': 'Manage criminal records in Fiji',
    'author': 'Your Name',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/person_views.xml',
    'views/criminal_record_views.xml',
    'views/conviction_views.xml',
    'views/relationship_views.xml',
    'views/address_views.xml',
    'views/fingerprint_views.xml',
    'views/menus.xml',  # <-- Add this line
],
    'installable': True,
    'application': True,
}
