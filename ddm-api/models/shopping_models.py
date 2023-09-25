
from flask_restx import fields

shop_model = {
    'ean': fields.String(required=False, description='Produktets EAN.'),
    'name': fields.String(required=True, description='Navnet på produktet.'),
    'brand': fields.String(required=False, description='Merkevaren til produktet.'),
    'count': fields.Integer(required=True, description='Antallet av produktet.'),
    'image': fields.String(required=False, description='Bilde'),
}

get_shop_model = {
    'id': fields.String(required=True, description='Produktets random id.'),
    'ean': fields.String(required=True, description='Produktets EAN.'),
    'name': fields.String(required=True, description='Navnet på produktet.'),
    'brand': fields.String(required=True, description='Merkevaren til produktet.'),
    'count': fields.Integer(required=True, description='Antallet av produktet.'),
    'uid': fields.String(required=True, description='Bruker-ID som eier produktet.'),
    'image': fields.String(required=False, description='Bilde'),
    'status': fields.Boolean(required=False, description='Status', default=False),
    'createdAt': fields.String(required=True, description='Datoen og tiden da produktet ble opprettet.')
}


update_shop_model = {
    'ean': fields.String(required=True, description='Produktets EAN.'),
    'name': fields.String(description='Navnet på produktet.'),
    'brand': fields.String(description='Merkevaren til produktet.'),
    'count': fields.Integer(description='Antallet av produktet.'),
    'status': fields.Boolean(required=False, description='Status'),
    'image': fields.String(description='Bilde')
}

