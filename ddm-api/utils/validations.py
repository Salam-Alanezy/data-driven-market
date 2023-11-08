from config import Config
def is_valid_api_key(api_key):
    
    valid_api_key = Config.XAPIKEY
    
    return api_key == valid_api_key