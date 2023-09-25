
from flask_restx import fields

mainCategoryModel = {
    'HovedkategoriID': fields.Integer(required=True, description='Unik identifikator for hovedkategorien'),
    'Hovedkategori': fields.String(required=True, description='Navnet på hovedkategorien')
}

subCategoryModel = {
    'HovedkategoriID': fields.Integer(required=True, description='Unik identifikator for hovedkategorien'),
    'UnderkategoriID': fields.Integer(required=True, dSescription='Unik identifikator for underkategorien'),
    'Underkategori': fields.String(required=True, description='NSavnet på underkategorien')
}

underCategoryModel = {
    'HovedkategoriID': fields.Integer(required=True, description='Unik identifikator for hovedkategorien'),
    'Hovedkategori': fields.String(required=True, description='Navnet på hovedkategorien'),
    'SegmentkategoriID': fields.Integer(required=True, description='Unik identifikator for segmentkategorien'),
    'Segmentkategori': fields.String(required=True, description='Navnet på segmentkategorien'),
    'UnderkategoriID': fields.Integer(required=True, description='Unik identifikator for underkategorien'),
    'Underkategori': fields.String(required=True, description='Navnet på underkategorien'),
    'ProduktID': fields.Integer(required=True, description='Unik identifikator for produktet'),
    'Produkt': fields.String(required=True, description='Navnet på produktet'),
    'Prioritetsnivå': fields.String(required=True, description='Prioritetsnivået for produktet'),
    'Beskrivelse': fields.String(required=True, description='Beskrivelsen av produktet')
}