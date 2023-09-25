
from flask_restx import fields

storageModel = {
    'ean': fields.String(required=True, description='Produktets EAN.'),
    'name': fields.String(required=True, description='Navnet på produktet.'),
    'brand': fields.String(required=True, description='Merkevaren til produktet.'),
    'count': fields.Integer(required=True, description='Antallet av produktet.'),
    'earliestExDate': fields.String(required=True, description='Den tidligste utløpsdatoen for produktet.'),
    'price': fields.Float(required=True, description='Prisen på produktet.'),
    'image': fields.String(required=True, description='Bilde.')
    
}

getStorageModel = {
    'id': fields.String(required=True, description='Produktets random id.'),
    'image': fields.String(required=True, description='Produktets bilde.'),
    'ean': fields.String(required=True, description='Produktets EAN.'),
    'name': fields.String(required=True, description='Navnet på produktet.'),
    'brand': fields.String(required=True, description='Merkevaren til produktet.'),
    'count': fields.Integer(required=True, description='Antallet av produktet.'),
    'earliestExDate': fields.String(required=True, description='Den tidligste utløpsdatoen for produktet.'),
    'price': fields.Float(required=True, description='Prisen på produktet.'),
    'uid': fields.String(required=True, description='Bruker-ID som eier produktet.'),
    'status': fields.Boolean(required=False, description='Status', default=False),
    'createdAt': fields.String(required=True, description='Datoen og tiden da produktet ble opprettet.')
}

updateStorageModel = {
    'ean': fields.String(required=True, description='Produktets EAN.'),
    'name': fields.String(description='Navnet på produktet.'),
    'brand': fields.String(description='Merkevaren til produktet.'),
    'count': fields.Integer(description='Antallet av produktet.'),
    'earliestExDate': fields.String(description='Den tidligste utløpsdatoen for produktet.'),
    'price': fields.Float(description='Prisen på produktet.'),
    'status': fields.Boolean(required=False, description='Status'),
    'image': fields.String(description='Bilde.')
}

def updateModel(get_storage_model): 
    return {
        'message': fields.String(description='Melding om oppdatering av produktet.'),
        'updated_data': fields.Nested(get_storage_model, description='Oppdaterte produktdata.')
        }