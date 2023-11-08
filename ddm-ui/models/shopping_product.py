import requests
from config import Config

def api_request(method, endpoint, payload=None):
    url = f"{Config.DMA_API_BASEURL}{endpoint}"
    headers = {
        'X-API-Key': Config.XAPIKEY,
        'uid': Config.UID,
        'Content-Type': 'application/json'
    }
    return requests.request(method, url, headers=headers, json=payload)

def get_all_shopping_products():
    response = api_request('GET', '/v1/shopping/get-all')
    return response.json()

def add_product_to_shopping(product_data):
    response = api_request('POST', '/v1/shopping/add-item', payload=product_data)
    return response.status_code == 200

def update_shopping_product(product_id, updated_data):
    endpoint = f"/v1/shopping/update-item/{product_id}"
    response = api_request('PUT', endpoint, payload=updated_data)
    return response.status_code == 200

def delete_shopping_product(product_id):
    endpoint = f"/v1/shopping/delete-item/{product_id}"
    response = api_request('DELETE', endpoint)
    return response.status_code == 200
