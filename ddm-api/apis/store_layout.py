from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
import random
from utils.validations import is_valid_api_key
from models.layout_model import layoutModel
api = Namespace('strategies', description='Gir tilgang til data om butikkprodukter og butikklayout.')

# Modell for butikklayout
store_layout_model = api.model('StoreLayout', layoutModel)


@api.route('/createStoreLayout')
class StoreLayout(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True))
    @api.expect(api.parser().add_argument('uid', location='headers', required=True))
    @api.expect(store_layout_model, validate=True)
    def post(self):
        try:
            # Get the API key from the header
            api_key = request.headers.get('X-API-Key')
            
            # Check if the API key is valid (you can implement your own logic here)
            if not is_valid_api_key(api_key):
                return {'message': 'Invalid API key'}, 401
            
            # Get the UID from the header
            uid = request.headers.get('uid')
            
            # Get the store layout data from the request payload
            store_layout_data = api.payload
            if type(store_layout_data) == list:
                for data in store_layout_data:
                    # Generate a random number to include in the document ID
                    random_number = random.randint(1000, 9999)
                    
                    # Add UID to each product row
                    data['uid'] = uid
                    
                    # Extract the ean field from the data
                    id = data.get('id')
                    
                    # Generate the document ID
                    document_id = f'{uid}-{id}-{random_number}'

                    data['uid'] = uid
                    # Set the store layout document ID as the UID
                    store_layout_ref = Config.db.collection('store-layout').document(document_id)
                    
                    # Set the store layout data in Firebase
                    store_layout_ref.set(data)
            
            return {'message': 'Store layout data inserted successfully'}, 201
        except Exception as e:
            return {'message': 'Unexpected error during store layout insertion: {}'.format(str(e))}, 500


@api.route('/getStoreLayoutById')
class GetStoreLayout(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True))
    @api.expect(api.parser().add_argument('uid', location='headers', required=True))
    def get(self):
        try:
            # Get the API key from the header
            api_key = request.headers.get('X-API-Key')
            
            # Check if the API key is valid (you can implement your own logic here)
            if not is_valid_api_key(api_key):
                return {'message': 'Invalid API key'}, 401
            
            # Get the UID from the header
            uid = request.headers.get('uid')
            
            # Retrieve all store layout documents with matching UID from Firebase
            store_layout_docs = Config.db.collection('store-layout').where('uid', '==', uid).get()
            
            # Initialize a list to store the store layout data
            store_layout_data = []
            
            # Iterate over the documents and extract the data
            for doc in store_layout_docs:
                store_layout_data.append(doc.to_dict())
            
            # Sort the store layout data based on the 'ID' field as integers
            store_layout_data.sort(key=lambda x: int(x['ID']))
            
            return store_layout_data, 200
        except Exception as e:
            return {'message': 'Unexpected error during store layout retrieval: {}'.format(str(e))}, 500

