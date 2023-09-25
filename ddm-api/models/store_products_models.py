
from flask_restx import fields


createProductModel = {
    'brand': fields.String(required=True, description='Navn på produkt leverandør'),
    'costPrice': fields.String(required=True, description='Salgsprisen på produktet'),
    'ean': fields.String(required=True, description='Strekkoden på produktet'),
    'name': fields.String(required=True, description='Navnet på produktet'),
    'priceExclVat': fields.String(required=True, description='Prisen eks. mva.'),
    'priceInclVat': fields.String(required=True, description='Prisen inkl. mva.')
    
}

getProductModel = {
    'brand': fields.String(required=True, description='Navn på produkt leverandør'),
    'costPrice': fields.String(required=True, description='Salgsprisen på produktet'),
    'ean': fields.String(required=True, description='Strekkoden på produktet'),
    'name': fields.String(required=True, description='Navnet på produktet'),
    'priceExclVat': fields.String(required=True, description='Prisen eks. mva.'),
    'priceInclVat': fields.String(required=True, description='Prisen inkl. mva.'),
    'uid':fields.String(required=True, description='Bruker id')
}
