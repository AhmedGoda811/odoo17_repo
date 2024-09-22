{
    'name': 'Custom Project Extension',
    'version': '1.0',
    'summary': 'Customizations for the Odoo Project module',
    'description': 'This module customizes the existing project module',
    'author': 'Ahmed Goda',
    'category': 'Project',
    'depends': ['project'],  
    'data': [ 'views/custom_project_view.xml',
            'security/ir.model.access.csv'
        
    ],
    
}
