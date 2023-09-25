from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
import random
from utils.validations import is_valid_api_key
from utils.logging_util import logger_config
from swagger_doc.store_products_swagger import *
from models.activities_models import scanProductModel, getScanModel

api = Namespace(name='store-ativities', description="Denne delen av API-et er for å hente inn informasjon av kassen i butikken.")

logger = logger_config(8, 'logs/store_activities.log')

# MODELS
create_product_model = api.model('createProduct', scanProductModel)
get_product_model = api.model('getProducts', getScanModel)




@api.route('/add-item')
class ScanProduct(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True), create_product_model, validate=True)

    @api.doc(description=post_description, security='apikey', params=params_post, responses=post_response)
    def post(self):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            
            product_data = api.payload
            uid = request.headers.get('uid') 
            
            if type(product_data) == list:
                
                for data in product_data:
                    random_number = random.randint(1000, 9999)
                    data['uid'] = uid
                    ean = data.get('ean')
                    document_id = ean
                    product_ref = Config.db.collection(Config.STORE_ACTIVITIES).document(document_id)
                    product_ref.set(data)
            else:
                random_number = random.randint(1000, 9999)
                product_data['uid'] = uid
                ean = product_data.get('strekkode', '')
                document_id = f'{uid}-{ean}-{random_number}'
                product_ref = Config.db.collection(Config.STORE_ACTIVITIES).document(document_id)
                product_ref.set(product_data)
            logger.info({'message': 'Produkter er lageret - status_kode 201'})
            return {'message': 'Produkter er lageret'}, 201
        except Exception as e:
            logger.info({'message': 'Uventet feil under innsetting av produktet:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under innsetting av produktet: {}'.format(str(e))}, 500




@api.route('/get-all')
class getAll(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    def get(self):

        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            
            uid = request.headers.get('uid')
            query = Config.db.collection(Config.STORE_ACTIVITIES).get()
            products = []
            
            for doc in query:
 
                if doc.get('uid') == uid:
                    product_data = doc.to_dict()
                    product_data['id'] = doc.id
                    products.append(product_data)
            logger.info({'message':"Hentet all produkt data med suksess - status_kode 200"})
            return product_data, 200
        except Exception as e:
            logger.error({'message': 'Uventet feil under produkthenting: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under produkthenting: {}'.format(str(e))}, 500

