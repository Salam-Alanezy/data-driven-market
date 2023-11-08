import os
from dotenv import load_dotenv
load_dotenv('.env')

class Config:

    # API
    BASEURL = os.getenv('BASEURL')
    # SECRET = os.getenv('SECRET')
    API_SECRET = os.environ.get('API_SECRET')


    DMA_API_BASEURL= os.getenv('DMA_API_BASEURL')
    XAPIKEY= os.getenv('XAPIKEY')
    UID=os.getenv('uid')
    # EMAIL
    EMAIL_CLIENT_ID = os.getenv('EMAIL_CLIENT_ID')
    EMAIL_SECRET = str(os.getenv('EMAIL_SECRET'))


    # APP
    PORT = int(os.getenv('PORT'))