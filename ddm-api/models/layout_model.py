
from flask_restx import fields

layoutModel = {
    'ID': fields.String(required=True, description='Unik identifikator for enheten'),
    'Enhetens Navn': fields.String(required=True, description='Navnet på enheten'),
    'Skilting Navn': fields.String(required=True, description='Navnet på skiltingen'),
    'Plassering i Butikken': fields.String(required=True, description='Plasseringen av enheten i butikken'),
    'Produktkategori': fields.String(required=True, description='Produktkategorien til enheten')
}
