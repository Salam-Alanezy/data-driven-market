import requests
from config import Config
from utils.logging_util import logger_config

# Config logger
logger = logger_config(7, 'logs/kassal_api.log')

def get_product(ean):
    url = f"https://kassal.app/api/v1/products/ean/{ean}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {Config.KASSAL_API}'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        
        if response.status_code == 200:
            res_json = response.json()
        else:
            logger.error({'message': f'Feil statuskode: {response.status_code}'})
            return None
    
    except requests.exceptions.RequestException as e:
        logger.error({'message': f'Feil under forespørsel: {str(e)}'})   
        return None

    except Exception as ex:
        logger.error({'message': f'Annen feil: {str(ex)}'})
        return None

    getEAN = res_json['data']['ean']
    getProducts = res_json['data']['products'][0]
    getName = getProducts['name']

    getVendor = getProducts['vendor']
    getBrand = getProducts['brand']
    getImage = getProducts['image']
    data = {
        'data': {
            'ean': str(getEAN),
            'products': [
                {
                    'name': str(getName),
                    'vendor': str(getVendor),
                    'brand': str(getBrand),
                    'image': str(getImage)
                }
            ]
        }
    }
    logger.info({'message': f'Dataen er hentet'})
    return data, response.status_code


def search_product(name):
    url = f"https://kassal.app/api/v1/products?search={name}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {Config.KASSAL_API}'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        
        if response.status_code == 200:
            res_json = response.json()
        else:
            logger.error({'message': f'Feil statuskode: {response.status_code}'})
            return None
    
    except requests.exceptions.RequestException as e:
        logger.error({'message': f'Feil under forespørsel: {str(e)}'})   
        return None

    except Exception as ex:
        logger.error({'message': f'Annen feil: {str(ex)}'})
        return None

    data_set = res_json['data'][0]
    
    
    getEAN = data_set['ean']
    getName = data_set['name']
    getVendor = data_set['vendor']
    getBrand = data_set['brand']
    getImage = data_set['image']
    data = {
        'data': {
            'ean': str(getEAN),
            'products': [
                {
                    'name': str(getName),
                    'vendor': str(getVendor),
                    'brand': str(getBrand),
                    'image': str(getImage)
                }
            ]
        }
    }
    logger.info({'message': f'Dataen er hentet'})
    return data, response.status_code
    


def get_all():
    
    url = f"https://kassal.app/api/v1/products"

    payload = {}
    headers = {
        'Authorization': f'Bearer {Config.KASSAL_API}'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        
        if response.status_code == 200:
            res_json = response.json()
        else:
            logger.error({'message': f'Feil statuskode: {response.status_code}'})
            return None
    
    except requests.exceptions.RequestException as e:
        logger.error({'message': f'Feil under forespørsel: {str(e)}'})   
        return None

    except Exception as ex:
        logger.error({'message': f'Annen feil: {str(ex)}'})
        return None

    # getEAN = res_json['data']['ean']
    # getProducts = res_json['data']['products'][0]
    # getName = getProducts['name']

    # getVendor = getProducts['vendor']
    # getBrand = getProducts['brand']
    # getImage = getProducts['image']
    # data = {
    #     'data': {
    #         'ean': str(getEAN),
    #         'products': [
    #             {
    #                 'name': str(getName),
    #                 'vendor': str(getVendor),
    #                 'brand': str(getBrand),
    #                 'image': str(getImage)
    #             }
    #         ]
    #     }
    # }
    # logger.info({'message': f'Dataen er hentet'})
    # return data, response.status_code
