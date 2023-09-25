from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
import random
from utils.validations import is_valid_api_key
import datetime
from models.shopping_models import shop_model, get_shop_model, update_shop_model
from swagger_doc.shopping_swagger import *
from utils.logging_util import logger_config

api = Namespace(Config.SHOPPING_COL, description='API-operasjoner relatert til handel liste. Dette API-et vil hovedsaklig bli brukt under bestillinger.')

# Config Logger
logger = logger_config(4, 'logs/shopping.log')

# MODELS
shopping_model = api.model('addShopping', shop_model)
get_shopping_model = api.model('getShopping', get_shop_model)
update_shopping_model = api.model('updateShopping', update_shop_model)

update_response_model = api.model('UpdateResponse', {
    'message': fields.String(description='Melding om oppdatering av produktet.'),
    'updated_data': fields.Nested(get_shopping_model, description='Oppdaterte produktdata.')
})

@api.route('/add-item')
class AddShoppingList(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True), 
                api.parser().add_argument('uid', location='headers', required=True),
                shopping_model, validate=True)
    @api.doc(description=post_description, params=params_post, responses=post_response)
    def post(self):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel -  status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            product_data = api.payload
            uid = request.headers.get('uid')
            current_time = datetime.datetime.now().isoformat()
            current_time_id = datetime.datetime.now()
            formatted_time = current_time_id.strftime(f"%d-%m-%Y")
            random_number = random.randint(1000, 9999)
            
            if type(product_data) == list:
                for data in product_data:
                                   
                    data['uid'] = uid
                    data['createdAt'] = current_time
                    data['id'] = f"{current_time}-{random_number}"
                    data['status'] = False

                    if data['ean'] == '' or data['ean'] == None:
                        data['ean'] = f"NOT ADDED - {random_number}"

                    ean = data.get('ean')
                    document_id = f"{ean}-{formatted_time}"
                    product_ref = Config.db.collection(Config.SHOPPING_COL).document(document_id)
                    product_ref.set(data)
            else:
                random_number = random.randint(1000, 9999)
                
                product_data['uid'] = uid
                product_data['createdAt'] = current_time
                product_data['status'] = False
                product_data['id'] = f"{current_time}-{random_number}"
                if product_data['ean'] == '' or product_data['ean'] == None:
                    product_data['ean'] = f"NOT ADDED - {random_number}"

                ean = product_data.get('ean')
                document_id = f"{ean}-{formatted_time}"
                product_ref = Config.db.collection(Config.SHOPPING_COL).document(document_id)
                product_ref.set(product_data)
                
            logger.info({'message': 'Produkter er lageret - status_kode 201'})
            return {'message': 'Produkter er lageret'}, 201
        except Exception as e:
            logger.info({'message': 'Uventet feil under innsetting av produktet:{} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under innsetting av produktet: {}'.format(str(e))}, 500

@api.route('/get-all')
class GetShoppingList(Resource):
    
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
            store_layout_docs = Config.db.collection(Config.SHOPPING_COL).where('uid', '==', uid).get()
            store_layout_data = []
            
            for doc in store_layout_docs:
                data = doc.to_dict()
                created_at = datetime.datetime.strptime(data['createdAt'], '%Y-%m-%dT%H:%M:%S.%f')
                data['createdAt'] = created_at.strftime('%d-%m-%Y')
                data['id'] = doc.id
                store_layout_data.append(data)
                
            logger.info({'message':"Hentet all produkt data med suksess - status_kode 200"})
            return store_layout_data, 200
        except Exception as e:
            logger.error({'message': 'Uventet feil under produkthenting: {} - status_kode 500'.format(str(e))})
            return {'message': 'Uventet feil under produkthenting: {}'.format(str(e))}, 500

@api.route('/update-item/<string:product_id>')
@api.doc(params={'product_id': 'Produktets random id.'})
class UpdateShoppingList(Resource):
    
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True),
                update_shopping_model, validate=True)
    @api.doc(description=update_description, params=params_update, responses=update_response)
    def put(self, product_id):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                return {'message': 'Invalid API key'}, 401

            uid = request.headers.get('uid')
            product_doc = Config.db.collection(Config.SHOPPING_COL).document(product_id).get()
            if not product_doc.exists or product_doc.to_dict().get('uid') != uid:
                return {'message': 'Product not found or does not belong to the user'}, 404

            update_data = api.payload
            current_time = datetime.datetime.now().isoformat()
            update_fields = {}
            
            for field in update_shopping_model.keys():
                if field in update_data:
                    update_fields[field] = update_data[field]

            if update_fields:
                Config.db.collection(Config.SHOPPING_COL).document(product_id).update(update_fields)

            updated_product_doc = Config.db.collection(Config.SHOPPING_COL).document(product_id).get()
            updated_data = updated_product_doc.to_dict()
            updated_data['createdAt'] = current_time
            updated_data['id'] = updated_product_doc.id
            
            return {'message': 'Product updated successfully', 'updated_data': updated_data}, 200
        except Exception as e:
            return {'message': 'Unexpected error during product update: {}'.format(str(e))}, 500


@api.route('/delete-item/<string:product_id>')
@api.doc(params={'product_id': 'Produktets random id.'})
class DeleteShoppingList(Resource):

    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True),
                api.parser().add_argument('uid', location='headers', required=True))
    @api.doc(description=delete_description,
             params=params_delete, responses=delete_response)
    def delete(self, product_id):
        try:
            api_key = request.headers.get('X-API-Key')
            
            if not is_valid_api_key(api_key):
                logger.error({'message': 'Ugyldig API-nøkkel - status_kode 401'})
                return {'message': 'Ugyldig API-nøkkel'}, 401

            uid = request.headers.get('uid')
            product_doc = Config.db.collection(Config.SHOPPING_COL).document(product_id).get()
            if not product_doc.exists or product_doc.to_dict().get('uid') != uid:
                logger.info({'message': 'Produktet er ikke funnet eller tilhører ikke brukeren - status_kode 404'})
                return {'message': 'Produktet er ikke funnet eller tilhører ikke brukeren'}, 404

            Config.db.collection(Config.SHOPPING_COL).document(product_id).delete()
            
            logger.info({'message': 'Produktet er slettet - status_kode 200'})
            return {'message': 'Produktet er slettet'}, 200
        except Exception as e:
            logger.info({'message': 'Uventet feil under sletting av produktet: - status_kode 500'})
            return {'message': 'Uventet feil under sletting av produktet: {}'.format(str(e))}, 500