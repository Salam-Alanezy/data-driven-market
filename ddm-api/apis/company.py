from flask import request
from flask_restx import Namespace, Resource, fields
from config import Config
from firebase_admin import auth, firestore
from datetime import datetime

api = Namespace('company', description='Company information APIs')


@api.route('/getCompany/<string:uid>')
class GetCompanyById(Resource):

    def get(self, uid):


        try:
            user_data = Config.db.collection('users').document(uid).get().to_dict()
            if user_data:
                user_data.pop('password', None)
                return user_data, 200
            else:
                return {'message': 'User not found'}, 404
        except Exception as e:
            return {'message': 'Unexpected error during profile retrieval: {}'.format(str(e))}, 500
        


@api.route('/getAll')
class GetAllCompanies(Resource):

    def get(self):
        try:
            user_profiles = []
            users_ref = Config.db.collection('users').stream()
            
            for user_doc in users_ref:
                user_data = user_doc.to_dict()
                user_data.pop('password', None) 
                user_profiles.append(user_data)
            
            return user_profiles, 200
        except Exception as e:
            return {'message': 'Unexpected error during profile retrieval: {}'.format(str(e))}, 500