from flask import request
from flask_restx import Namespace, Resource
from config import Config
import requests
from utils.validations import is_valid_api_key
from utils.logging_util import logger_config
from models.category_models import mainCategoryModel, subCategoryModel, underCategoryModel
from swagger_doc.categories_swagger import *

api = Namespace(name=ns_name, description=ns_description)

logger = logger_config(1, 'logs/categories.log')

main_category_model = api.model('MainCategory', mainCategoryModel)

sub_category_model = api.model('SubCategory', subCategoryModel)

category_model = api.model('Category', underCategoryModel)

@api.route('/create-main-categories')
class MainCategories(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True),
                main_category_model, validate=True)
    @api.doc(
        description=post_description,
        params=params_post,
        body=main_category_model,
        responses=post_response
    )
    def post(self):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            uid = request.headers.get('uid')
            main_category_importance_data = api.payload 

            if isinstance(main_category_importance_data, list):
                for data in main_category_importance_data:
                    try:
                        hovedkategori_id = data.get('HovedkategoriID')
                        document_id = f'{uid}-{hovedkategori_id}'
                        main_category_importance_ref = Config.db.collection(Config.MAIN_CATEGORY_COL).document(document_id)
                        main_category_importance_ref.set(data)
                    except Exception as e:
                        logger.error({'message': 'Feil under for-loop '})
                        logger.error({'ERROR': e})
                        return {'message': 'Ugyldig API-nøkkel', 'ERROR': e}
                    
            elif isinstance(main_category_importance_data, dict):
                try:
                    hovedkategori_id = main_category_importance_data.get('HovedkategoriID')
                    document_id = f'{uid}-{hovedkategori_id}'
                    main_category_importance_ref = Config.db.collection(Config.MAIN_CATEGORY_COL).document(document_id)
                    main_category_importance_ref.set(main_category_importance_data)
                except Exception as e:
                    logger.error({"message': 'Error under legge til 'dict' data til database!"})
                    logger.error({'ERROR': e})
                    return {'message': 'Ugyldig API-nøkkel', 'ERROR': e}
            else:
                logger.error({'message': 'Ugyldige data for viktighet av hovedkategori - status_kode 400'})
                return {'message': 'Ugyldige data for viktighet av hovedkategori'}, 400
            
            logger.info({"message": "Hovedkategorien ble lagt til med suksess - status_kode 201"})
            return {'message': 'Hovedkategorien ble lagt til med suksess'}, 201
        except Exception as e:
            
            logger.info({"message": 'Uventet feil under tillegging av viktighet for hovedkategori: {} - status_kode 500'.format(str(e)) })
            return {'message': 'Uventet feil under tillegging av viktighet for hovedkategori: {}'.format(str(e))}, 500

@api.route('/get-main-categories')
class GetMainCategories(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(
        description=get_description,
        params=params,
        responses=get_response
    )
    def get(self):

        try:
            api_key = request.headers.get('X-API-Key')
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            uid = request.headers.get('uid')
            main_categories_docs = Config.db.collection(Config.MAIN_CATEGORY_COL).where('uid', '==', uid).get()
            main_categories_data = []

            for doc in main_categories_docs:
                main_categories_data.append(doc.to_dict())
            
            logger.info('Hovedkategorien ble hentet med suksess') 
            return main_categories_data, 200
        except Exception as e:
            logger.error({'message': 'Uventet feil under henting av hovedkategorier: {}'.format(str(e))})
            return {'message': 'Uventet feil under henting av hovedkategorier: {}'.format(str(e))}, 500

@api.route('/sub-categories')
class SubCategories(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(
        description=get_sub_description,
        params=params,
        responses= get_sub_response
    )
    def get(self):
        api_key = request.headers.get('X-API-Key')
        
        if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/sub-categories.json')
            data = response.json()

            logger.info( {'message': 'Sub-kategorien ble hentet med suksess - status_kode 200'})
            return data, 200
        except requests.ConnectionError as ce:
            logger.error( {'message': str(ce) + ' - status_kode 401'})
            return {'message': str(ce)}, 401
        except Exception as e:
            logger.error({'message': 'Uventet feil under henting av underkategorier: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under henting av underkategorier: {}'.format(str(e))}, 500
        
@api.route('/categories')
class Categories(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(        
        description=get_all_description,
        params=params,
        responses=get_all_response
    )
    def get(self):
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/categories.json')
            data = response.json()
            logger.info({'message': 'Kategorier ble hentet med suksess - status_kode 200'})
            return data, 200
        except requests.ConnectionError as ce:
            logger.error({'message': str(ce) + ' - status_kode 401'}  )
            return {'message': str(ce)}, 401
        except Exception as e:
            logger.error({'message': 'Uventet feil under henting av kategorier: {} -  status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under henting av kategorier: {}'.format(str(e))}, 500