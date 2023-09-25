
from flask_restx import fields


geoModel = {
    'ID': fields.Integer(required=True, description='Unik identifikator for bydel'),
    'district': fields.String(required=True, description='Navn på bydel')
}

areaModel = {
    'districtID': fields.Integer(required=True, description='Identifikator til bydel'),
    'area': fields.String(required=True, description='Navnet på område'),
}
