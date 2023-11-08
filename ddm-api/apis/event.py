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


# Liste over de ønskede feltene
desired_fields = [
    "Event/Holiday",
    "Description",
    "FocusGroup",
    "TypicalGoodsinHighDemand",
    "DigitalMarketingExamples",
    "MarketingLocation",
    "PreparationTips",
    "EstimatedBudget",
    "image"
]

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

            for doc in events_docs:
                full_data = doc.to_dict()
                # Filtrer ut kun de ønskede feltene
                filtered_data = {key: full_data[key] for key in desired_fields if key in full_data}
                events_data.append(filtered_data)
                
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

