from flask import request
from flask_restx import Namespace, Resource
from config import Config
import random
from utils.validations import is_valid_api_key
import datetime
import  data_manipulation.ninja_api as ra
from models.event_models import eventModel, getEventModel
from swagger_doc.events_swagger import *
from utils.logging_util import logger_config



api = Namespace(name=ns_name, description=ns_description)

# Config logger
logger = logger_config(5, 'logs/events.log')

# MODELS
event_model = api.model('Event', eventModel)
get_event_model = api.model('GetEvent', getEventModel)

@api.route('/create-event')
class Events(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True),
                event_model, validate=True)
    @api.doc(description=post_description, params=params_post, responses=post_response)
    def post(self):
        try:
            api_key = request.headers.get('X-API-Key')

            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            event_data = api.payload
            uid = request.headers.get('uid')
            current_time = datetime.datetime.now().isoformat()
            random_number = random.randint(1000, 9999)
            
            event_data['uid'] = uid
            event_data['createdAt'] = current_time
            event_data['id'] = f"{current_time}-{random_number}"

            document_id = f"{event_data['Date']}-{event_data['Event/Holiday']}"
            
            event_ref = Config.db.collection('events').document(document_id)
            event_ref.set(event_data)

            logger.info({'message': 'Eventet er lageret - status_kode 201'})
            return {'message': 'Eventet er lageret'}, 201
        except Exception as e:
            logger.info({'message': 'Uventet feil under innsetting av produktet:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under innsetting av produktet: {}'.format(str(e))}, 500

@api.route('/get-all')
class GetEvents(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(description=get_description, params=params, responses=get_response)
    def get(self):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            
            uid = request.headers.get('uid')
            events_docs = Config.db.collection('events').where('uid', '==', uid).get()
            events_data = []
            current_year = datetime.datetime.now().year

            for doc in events_docs:
                data = doc.to_dict()
                date_parts = data['Date'].split('-')
                data['Date'] = f"{date_parts[0].zfill(2)}-{date_parts[1].zfill(2)}-{current_year}"
                marketing_start_date_parts = data['MarketingStartDate'].split('-')
                data['MarketingStartDate'] = f"{marketing_start_date_parts[0].zfill(2)}-{marketing_start_date_parts[1].zfill(2)}-{current_year}"
                marketing_end_date_parts = data['MarketingEndDate'].split('-')
                data['MarketingEndDate'] = f"{marketing_end_date_parts[0].zfill(2)}-{marketing_end_date_parts[1].zfill(2)}-{current_year}"
                
                events_data.append(data)
            logger.info({'message':"Hentet all event data med suksess - status_kode 200"})
            return events_data, 200
        
        except Exception as e:
            logger.error({'message': 'Uventet feil under datahenting: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under datahenting: {}'.format(str(e))}, 500

@api.route('/ninja-events/<string:country>/<string:year>')
class getEventsNinja(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(params=params_ninja, responses=get_ninja_response)
    def get(self, country, year):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            
            uid = request.headers.get('uid')
            events_docs = ra.get_holidays(country, year)
            logger.info({'message':"Hentet all event data i fra Ninja API - status_kode 200"})
            return events_docs, 200
        
        except Exception as e:
            logger.error({'message': 'Uventet feil under produkthenting: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under produkthenting: {}'.format(str(e))}, 500

