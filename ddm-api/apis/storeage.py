from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
import random
from utils.validations import is_valid_api_key
from utils.logging_util import logger_config
import datetime
from models.storage_models import storageModel, getStorageModel, updateStorageModel, updateModel
from swagger_doc.storage_swagger import * 
api = Namespace(name=ns_name, description=ns_description)


logger = logger_config(3, 'logs/storage.log')

# MODELS
storage_model = api.model('Storage', storageModel)
get_storage_model = api.model('getStorage', getStorageModel)
update_storage_model = api.model('UpdateStorage', updateStorageModel)


@api.route('/add-item')
class AddToStorage(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True),
                storage_model, validate=True)
    @api.doc(description=post_description, 
             responses=post_response, params=params)
    def post(self):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            product_data = api.payload
            uid = request.headers.get('uid')
            current_time = datetime.datetime.now().isoformat()
            current_time_id = datetime.datetime.now()
            formatted_time = current_time_id.strftime(f"%d-%m-%Y")
            
            if type(product_data) == list:
                
                for data in product_data:
                    data['uid'] = uid
                    data['createdAt'] = current_time
                    data['status'] = False
                    ean = data.get('ean')
                    document_id = f"{ean}-{formatted_time}"
                    product_ref = Config.db.collection(Config.STORAGE_COL).document(document_id)
                    product_ref.set(data)
            else:
                product_data['uid'] = uid
                product_data['createdAt'] = current_time
                product_data['status'] = False
                ean = product_data.get('ean')
                document_id = f"{ean}-{formatted_time}"
                product_ref = Config.db.collection(Config.STORAGE_COL).document(document_id)
                product_ref.set(product_data)
            
            logger.info({'message': 'Produkted er lageret i database - status_kode 201'})
            return {'message': 'Produkted er lageret i database'}, 201
        except Exception as e:
            logger.info({'message': 'Uventet feil under innsetting av produktet: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under innsetting av produktet: {}'.format(str(e))}, 500

@api.route('/get-all')
class GetStorage(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(description=get_description, params=params,
        responses=get_response)
    def get(self):
        try:
            api_key = request.headers.get('X-API-Key')
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel'})
                return {'message': 'Ugyldig API-nøkkel'}, 401
           
            uid = request.headers.get('uid')
            store_layout_docs = Config.db.collection(Config.STORAGE_COL).where('uid', '==', uid).get()
            store_layout_data = []
            
            for doc in store_layout_docs:
                data = doc.to_dict()
                created_at = datetime.datetime.strptime(data['createdAt'], '%Y-%m-%dT%H:%M:%S.%f')
                data['createdAt'] = created_at.strftime('%d-%m-%Y')
                data['id'] = doc.id
                store_layout_data.append(data)
            logger.info({'message': 'Produkt data ble hentet - status_kode 200'})
            return store_layout_data, 200
        except Exception as e:
            logger.error({'message': 'Unexpected error during store layout retrieval: {} - status_kode 500'.format(str(e))})
            return {'message': 'Unexpected error during store layout retrieval: {}'.format(str(e))}, 500

@api.route('/update-item/<string:product_id>')
@api.doc(params={'product_id': 'Produktets random id.'})
class UpdateStorage(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True),
                update_storage_model, validate=True)

    @api.doc(description=update_description,
             params=params_product_id, responses=update_response)
    def put(self, product_id):
        try:
            api_key = request.headers.get('X-API-Key')

            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            uid = request.headers.get('uid')
            product_doc = Config.db.collection(Config.STORAGE_COL).document(product_id).get()
            if not product_doc.exists or product_doc.to_dict().get('uid') != uid:
                logger.error({'message': 'Produktet er ikke funnet eller tilhører ikke brukeren - status_kode 404'})
                return {'message': 'Produktet er ikke funnet eller tilhører ikke brukeren'}, 404

            update_data = api.payload
            current_time = datetime.datetime.now().isoformat()
            update_fields = {}
            
            for field in update_storage_model.keys():
                
                if field in update_data:
                    update_fields[field] = update_data[field]

            if update_fields:
                Config.db.collection(Config.STORAGE_COL).document(product_id).update(update_fields)

            updated_product_doc = Config.db.collection(Config.STORAGE_COL).document(product_id).get()
            updated_data = updated_product_doc.to_dict()
            updated_data['createdAt'] = current_time
            updated_data['id'] = updated_product_doc.id
            logger.info({'message': 'Produktet ble oppdatert - status_kode 200'})
            return {'message': 'Produktet ble oppdatert', 'Oppdaterte data': updated_data}, 200
        except Exception as e:
            logger.error({'message': 'Uventet feil under produktoppdatering: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under produktoppdatering: {}'.format(str(e))}, 500
                
@api.route('/delete-item/<string:product_id>')
@api.doc(params={'product_id': 'Produktets random id.'})
class DeleteStorage(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(description=delete_description, params=params_product_id, responses=delete_response)
    def delete(self, product_id):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            uid = request.headers.get('uid')
            product_doc = Config.db.collection(Config.STORAGE_COL).document(product_id).get()
            
            if not product_doc.exists or product_doc.to_dict().get('uid') != uid:
                logger.info({'message': 'Produktet er ikke funnet eller tilhører ikke brukeren - status_kode 404'})
                return {'message': 'Produktet er ikke funnet eller tilhører ikke brukeren'}, 404

            Config.db.collection(Config.STORAGE_COL).document(product_id).delete()
            logger.info({'message': 'Produktet er slettet - status_kode 200'})
            return {'message': 'Produktet er slettet'}, 200
        except Exception as e:
            logger.info({'message': 'Uventet feil under sletting av produktet: - status_kode 500'})
            return {'message': 'Uventet feil under sletting av produktet: {}'.format(str(e))}, 500