from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
from models.strategies_models import productStrategyModel, holidaysModel
import requests

api = Namespace('strategy', description='Gir tilgang til data for produktstrategi for bedre forståelse av dagligvareprodukter.')

# Modell for produktstrategi
product_strategy_model = api.model('ProductStrategy', productStrategyModel)

holidays_model = api.model('Holidays', holidaysModel)

@api.route('/product-strategy')
class ProductStrategy(Resource):
    @api.doc(security='apikey', description='Henter all produktstrategi')
    @api.marshal_list_with(product_strategy_model)
    def get(self):
        """
        Henter all produktstrategi
        """
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/product-strategy.json')
            data = response.json()
        
            return data, 200
        except requests.ConnectionError as ce:
            return {'message': str(ce)}, 401
        except Exception as e:
            return {'message': 'Uventet feil: {}'.format(str(e))}, 500

@api.route('/holidays')
class Holidays(Resource):
    @api.doc(security='apikey', description='Henter all viktige datoer for markedsføring')
    @api.marshal_list_with(holidays_model)
    def get(self):
        """
        Henter all viktige datoer for markedsføring
        """
        try:
            response = requests.get(Config.JSON_BASE_PATH + '/holidays.json')
            data = response.json()
        
            return data, 200
        except requests.ConnectionError as ce:
            return {'message': str(ce)}, 401
        except Exception as e:
            return {'message': 'Uventet feil: {}'.format(str(e))}, 500
