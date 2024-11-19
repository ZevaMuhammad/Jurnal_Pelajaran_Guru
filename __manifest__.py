{
    'name': 'Jurnal Mengajar',
    'version': '1.0',
    'summary': 'Modul untuk manajemen jurnal mengajar di Odoo 18',
    'author': 'Pengembang',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/dashboard.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "jurnal_mengajar/static/src/css/dashboard.css",
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
