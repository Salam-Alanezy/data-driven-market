import requests
from config import Config
import json

class APIHandler: 
            
    def get_ddma(endpoint):
        # API URI
        uri = f"{Config.DMA_API_BASEURL}{endpoint}"
        # API HEADER
        headers = {
            'X-API-Key': Config.XAPIKEY,
            'uid': Config.UID}
        # GET REQUEST
        try:
            response = requests.get(uri, headers=headers)
            if response.status_code == 200:
                raw_products = response.json()
                return raw_products
            else:
                return {'Error': 'COULD NOT CALL THE DDMA-API'}       
        except Exception as e:
            print(f'ERROR: {str(e)}')
    
    def get_kassal(ean):
        baseURL = Config.BASEURL
        header = {'Authorization': Config.API_SECRET}
        endpoint = f"{baseURL}/{ean}"
        try:
            response = requests.get(endpoint, headers=header)
            if response.status_code == 200:
                response = response.json()
                response['status'] = 200   
                return response
            else:
                return {'Error': 'Could not call the kassal API'}
        except Exception as e:
            print(f'ERROR - KASSAL API: {str(e)}' )
            
    def add_ddma(endpoint, payload):
        uri = f"{Config.DMA_API_BASEURL}{endpoint}" # Replace with the actual API endpoint URL
        headers = {
            'X-API-Key': Config.XAPIKEY,
            'uid': Config.UID
        }
        response = requests.post(uri + endpoint, headers=headers, data=payload)
        return response