from flask import request
from flask_restx import Namespace, Resource
from utils.validations import is_valid_api_key
from utils.logging_util import logger_config
from swagger_doc.kassal_swagger import * 
from data_manipulation.kassal_api import get_product, search_product, get_all

api = Namespace(name=ns_name, description=ns_description)

logger = logger_config(6, 'logs/store_products.log')

@api.route('/get-item/<ean>')
class getProduct(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))

    @api.doc(description=get_description, params=get_params, responses=get_response)
    
    def get(self, ean):
        
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            data, status_code = get_product(ean) 
            
            if status_code == 200: 
                return data
            else:
                logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
                return {'message': f'Uventet feil under henting av Kassal-API data - status_kode {str(status_code)}'}
        except Exception as e:
            logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under henting av Kassal-API data{}'.format(str(e))}, 500




@api.route('/search-item/<name>')
class searchProduct(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))

    @api.doc(description=get_description, params=search_params, responses=get_response)
    
    def get(self, name):
        
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            data, status_code = search_product(name) 
            
            if status_code == 200: 
                return data
            else:
                logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
                return {'message': f'Uventet feil under henting av Kassal-API data - status_kode {str(status_code)}'}
        except Exception as e:
            logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under henting av Kassal-API data{}'.format(str(e))}, 500


@api.route('/get-all')
class getAll(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))

    @api.doc(description=all_description, params=all_params, responses=all_response)
    
    def get(self):
        
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
            data, status_code = get_all() 
            
            if status_code == 200: 
                return data
            else:
                logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
                return {'message': f'Uventet feil under henting av Kassal-API data - status_kode {str(status_code)}'}
        except Exception as e:
            logger.info({'message': 'Uventet feil under henting av Kassal-API data:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under henting av Kassal-API data{}'.format(str(e))}, 500


