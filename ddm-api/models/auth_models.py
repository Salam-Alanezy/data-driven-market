
from flask_restx import fields

loginModel = {
    'email': fields.String(required=True, description='Brukerens e-post'),
    'password': fields.String(required=True, description='Brukerens passord')

}

registrationModel = {
    'email': fields.String(required=True, description="Brukerens e-postadresse"),
    'password': fields.String(required=True, description="Brukerens passord"),
    'display_name': fields.String(required=True, description="Brukerens visningsnavn")
}
