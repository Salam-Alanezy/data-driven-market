from flask_restx import Namespace, Resource, fields
from config import Config
import requests
from models.geo_models import geoModel, areaModel

api = Namespace('geo', description='Gir tilgang til data for bydeler og områder i Oslo.')

geo_model = api.model('Regions', geoModel)

areas_model = api.model('Area', areaModel)


@api.route('/oslo-region')
class OsloGeoRegion(Resource):
    @api.doc(security='apikey', description='Henter all områder i oslo etter bydel')
    @api.marshal_list_with(areas_model)
    def get(self):
        """
        Henter all områder i Oslo
        """
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/oslo-regions.json')
            data = response.json()
        
            return data, 200
        except requests.ConnectionError as ce:
            return {'message': str(ce)}, 401
        except Exception as e:
            return {'message': 'Uventet feil: {}'.format(str(e))}, 500


@api.route('/oslo-areas')
class OsloGeoArea(Resource):
    @api.doc(security='apikey', description='Henter all områder i oslo etter bydel')
    @api.marshal_list_with(areas_model)
    def get(self):
        """
        Henter all områder i Oslo
        """
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/oslo-areas.json')
            data = response.json()
        
            return data, 200
        except requests.ConnectionError as ce:
            return {'message': str(ce)}, 401
        except Exception as e:
            return {'message': 'Uventet feil: {}'.format(str(e))}, 500


