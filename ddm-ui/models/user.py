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

def login_user(email, password):
    payload = {'email': email, 'password': password}
    response = api_request('POST', '/v1/auth/login', payload)
    return response

def get_all_storage():
    response = api_request('GET', '/v1/storage/get-all')
    return response.json()

