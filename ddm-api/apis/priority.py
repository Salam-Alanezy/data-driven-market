from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
import bcrypt
import requests

api = Namespace('prio', description='Gir tilgang til data for organisering av dagligvareprodukter ved å presentere hierarkisk struktur, underkategorier og produktstrategi for bedre navigasjon og forståelse.')

main_category_importance_model = api.model('MainCategoryImportance', {
    'HovedkategoriID': fields.Integer(required=True, description='Unik identifikator for hovedkategorien'),
    'Viktighet': fields.String(required=True, description='Viktighet for hovedkategorien'),
    'Prioriteringsnivå': fields.String(required=True, description='Prioritetsnivå for hovedkategorien'),
    'Beskrivelse av viktigheten': fields.String(required=True, description='Beskrivelse av viktigheten'),
    'Beskrivelse av Prioriteringsnivå': fields.String(required=True, description='Beskrivelse av prioritetsnivået')
})

sub_category_importance_model = api.model('SubCategoryImportance', {
    'UnderkategoriID': fields.Integer(required=True, description='Unik identifikator for underkategorien'),
    'Prioriteringsnivå': fields.String(required=True, description='Prioritetsnivå for underkategorien'),
    'Viktighet': fields.String(required=True, description='Viktighet for underkategorien'),
    'Beskrivelse av viktigheten': fields.String(required=True, description='Beskrivelse av viktigheten'),
    'Beskrivelse av Prioriteringsnivå': fields.String(required=True, description='Beskrivelse av prioritetsnivået')
})

@api.route('/main-categories')
class MainCategories(Resource):
    @api.expect(api.parser().add_argument('X-API-Key', location='headers', required=True))
    @api.expect(api.parser().add_argument('uid', location='headers', required=True))
    @api.expect(main_category_importance_model, validate=True)
    def post(self):
        """
        Legger til viktighet av hovedkategorier
        """
        try:
            api_key = request.headers.get('X-API-Key')

            if not is_valid_api_key(api_key):
                return {'message': 'Invalid API key'}, 401
            
            uid = request.headers.get('uid')
            main_category_importance_data = api.payload

            if isinstance(main_category_importance_data, list):

                for data in main_category_importance_data:
                    hovedkategori_id = data.get('HovedkategoriID')
                    document_id = f'{uid}-{hovedkategori_id}'
                    main_category_importance_ref = Config.db.collection('main-categories').document(document_id)
                    main_category_importance_ref.set(data)
            elif isinstance(main_category_importance_data, dict):
     
                hovedkategori_id = main_category_importance_data.get('HovedkategoriID')
                document_id = f'{uid}-{hovedkategori_id}'
                main_category_importance_ref = Config.db.collection('main-categories').document(document_id)
                main_category_importance_ref.set(main_category_importance_data)
            else:
                return {'message': 'Invalid main category importance data'}, 400
            
            return {'message': 'Main category importance added successfully'}, 201
        except Exception as e:
            return {'message': 'Unexpected error during main category importance addition: {}'.format(str(e))}, 500



@api.route('/sub-categories')
class SubCategories(Resource):
    @api.doc(security='apikey', description='Henter alle underkategorier med viktighet og prioritetsnivå')
    @api.marshal_list_with(sub_category_importance_model)
    def get(self):
        """
        Henter alle underkategorier med viktighet og prioritetsnivå
        """
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/sub-categories-importance.json')
            data = response.json()
        
            return data, 200
        except requests.ConnectionError as ce:
            return {'message': str(ce)}, 401
        except Exception as e:
            return {'message': 'Uventet feil: {}'.format(str(e))}, 500



def is_valid_api_key(api_key):
    valid_api_key = Config.XAPIKEY
    return api_key == valid_api_key