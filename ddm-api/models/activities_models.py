
from flask_restx import fields


scanProductModel = {
    'ean': fields.String(required=True, description='Strekkoden på produktet'),
    
}

getScanModel = {
    'brand': fields.String(required=True, description='Navn på produkt leverandør'),
    'costPrice': fields.String(required=True, description='Salgsprisen på produktet'),
    'ean': fields.String(required=True, description='Strekkoden på produktet'),
    'name': fields.String(required=True, description='Navnet på produktet'),
    'createdAt': fields.DateTime(required=True, description='Timestamp for skanning av produktet i kassen'),
    'uid':fields.String(required=True, description='Bruker id')
}
