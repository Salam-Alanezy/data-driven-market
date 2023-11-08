import requests
from config import Config
import json

def api_request(method, endpoint, payload=None):
    url = f"{Config.DMA_API_BASEURL}{endpoint}"
    headers = {
        'X-API-Key': Config.XAPIKEY,
        'uid': Config.UID,
        'Content-Type': 'application/json'
    }
    return requests.request(method, url, headers=headers, json=payload)

def api_updated_request(method, endpoint, payload=None):
    url = f"{Config.DMA_API_BASEURL}{endpoint}"
    headers = {
        'X-API-Key': Config.XAPIKEY,
        'uid': Config.UID,
        'Content-Type': 'application/json'
    }
    return requests.request(method, url, headers=headers, data=payload)

def get_all_products():
    response = api_request('GET', '/v1/storage/get-all')
    return response.json()


def get_by_ean(ean):
    response = api_request('GET', f'/v1/store/get-item/{ean}')
    return response
    
def add_product_to_storage(product_data):
    response = api_request('POST', '/v1/storage/add-item', payload=product_data)
    return response.status_code == 200

def update_product_in_storage(product_id, updated_data):
    response = api_updated_request('PUT', f"/v1/storage/update-item/{product_id}", updated_data)
    if response.status_code == 200:
        return response
    else:
        return {'message': 'Something went woring in update_product_in_storage'}
def delete_product_from_storage(product_id):
    endpoint = f"/v1/storage/delete-item/{product_id}"
    response = api_request('DELETE', endpoint)
    return response.status_code == 200
