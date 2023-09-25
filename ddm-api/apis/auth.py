from flask import request
from flask_restx import Namespace, Resource
from config import Config
from firebase_admin import auth
import bcrypt
import datetime
from utils.validations import is_valid_api_key
from utils.hstring import verify_password
from models.auth_models import loginModel, registrationModel
from swagger_doc.auth_swagger import *
from utils.logging_util import logger_config


api = Namespace(name=ns_name, description=ns_description)

# Config the logger
logger = logger_config(2, 'logs/auth.log')

# MODELS
user_login_model = api.model('UserLogin', loginModel)
user_registration_model = api.model('UserRegistration', registrationModel)

@api.route('/login')
class UserLogin(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), user_login_model, validate=True)
    @api.marshal_with(user_login_model)
    @api.doc(description=login_description, params=params , responses=login_response)
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            
            user = auth.get_user_by_email(email)
            uid = user.uid
            user_ref = Config.db.collection(Config.AUTH_COL).document(uid)
            user_snapshot = user_ref.get()
            
            if user_snapshot.exists:
                user_data = user_snapshot.to_dict()
                hashed_password = user_data.get('password')
                if verify_password(password, hashed_password):
                    timestamp = datetime.datetime.now().isoformat()
                    logger.info({'message': f'Bruker logget inn tid: {timestamp} -  status_kode 200'})
                    return {'message': 'Bruker logget inn', 'uid': uid, 'timestamp': timestamp}, 200
                else:
                    logger.error({'message': 'Ugyldig legitimasjon - status_kode 401'})
                    return {'message': 'Ugyldig legitimasjon'}, 401
            else:
                logger.error({'message': 'Ugyldig legitimasjon - status_kode 401'})
                return {'message': 'Ugyldig legitimasjon'}, 401

        except auth.UserNotFoundError as ae:
            logger.error({'message': f'Ugyldig legitimasjon - {str(ae)} -  status_kode 401'})
            return {'message': 'Ugyldig legitimasjon'}, 401

        except Exception as e:
            logger.error({'message': 'Uventet feil under pålogging: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under pålogging: {}'.format(str(e))}, 500

@api.route('/register')
class UserRegistration(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                user_registration_model, validate=True)
    @api.doc(description=register_description, params=params , responses=register_response)
    def post(self):

        api_key = request.headers.get('X-API-Key')

        if not is_valid_api_key(api_key):
            logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
            return {'message': 'Ugyldig API-nøkkel'}, 401

        data = request.json
        email = data.get('email')
        password = data.get('password')
        display_name = data.get('display_name')
        timestamp = datetime.datetime.now().isoformat()

        try:
            existing_user = auth.get_user_by_email(email)
            logger.error({'message': 'Bruker med samme e-postadresse finnes allerede -  status_kode 409'})
            return {'message': 'Bruker med samme e-postadresse finnes allerede'}, 409
        except auth.UserNotFoundError:
            logger.error({'message': 'Uventet feil under brukerregistrering: {}'.format(str(auth.UserNotFoundError))})
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            try:
                user = auth.create_user(
                    email=email,
                    password=password
                )

                user_data = {
                    'email': email,
                    'password': hashed_password.decode('utf-8'),
                    'display_name':display_name,
                    'createdAt': timestamp,
                    'uid':user.uid
                }
                Config.db.collection(Config.AUTH_COL).document(user.uid).set(user_data)
                logger.info({'message': f'Brukeren er registrert - createdAt: {str(timestamp)} -  status_kode 201'})
                return {'message': 'Brukeren er registrert ', 'createdAt': timestamp}, 201
            except auth.AuthError as e:
                logger.error({'message': 'Feil ved oppretting av bruker: {} - status_kode 500'.format(str(e))})
                return {'message': 'Feil ved oppretting av bruker: {}'.format(str(e))}, 500
            except Exception as e:
                logger.error({'message': 'Uventet feil under registrering: {} - status_kode 500'.format(str(e))})
                return {'message': 'Uventet feil under registrering: {}'.format(str(e))}, 500
        except Exception as e:
            logger.error({'message': 'Uventet feil under registrering: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under registrering: {}'.format(str(e))}, 500