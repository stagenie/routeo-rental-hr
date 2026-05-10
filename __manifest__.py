{
    'name': 'Routeo Rental HR',
    'version': '19.0.1.0.0',
    'category': 'Services/Rental',
    'summary': "Extension RH de Routeo Rental — emprunts internes avec remise employé",
    'author': 'OdooSkills',
    'website': 'https://odooskills.com',
    'license': 'LGPL-3',
    'depends': ['routeo_rental', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/routeo_rental_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
