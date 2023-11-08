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



def get_product_by_ean(ean):
    response = api_request('GET', f'/v1/kassal/get-item/{ean}') 
    return response
   
   
    