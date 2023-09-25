import os 
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import json 

load_dotenv()

class Config:

    PORT = int(os.getenv('PORT'))

    SSB_BASE_URL = os.getenv('SSB_BASE_URL') 
    JSON_BASE_PATH = os.getenv('JSON_BASE_PATH') 
    
    # Kassal-API
    KASSAL_API = os.getenv('KASSAL_API')

      # Firebase
    PRIVATE_KEY = os.getenv('PRIVATE_KEY').replace('\\n', '\n') # Replace escaped newlines
    TYPE = os.getenv('TYPE')
    PROJECT_ID = os.getenv('PROJECT_ID')
    PRIVATE_KEY_ID = os.getenv('PRIVATE_KEY_ID')
    CLIENT_EMAIL = os.getenv('CLIENT_EMAIL')
    CLIENT_ID = os.getenv('CLIENT_ID')
    AUTH_URI = os.getenv('AUTH_URI')
    TOKEN_URI = os.getenv('TOKEN_URI')
    AUTH_PROVIDER_X509_CERT_URL = os.getenv('AUTH_PROVIDER_X509_CERT_URL')
    CLIENT_X509_CERT_URL = os.getenv('CLIENT_X509_CERT_URL')
    UNIVERSE_DOMAIN = os.getenv('UNIVERSE_DOMAIN')

    PORT = int(os.getenv('PORT'))

    NINJAXApiKey = os.getenv('NINJAXApiKey')
    
    firebase_config = {
    "type": TYPE,
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": PRIVATE_KEY,  
    "client_email": CLIENT_EMAIL,
    "client_id": CLIENT_ID,
    "auth_uri": AUTH_URI,
    "token_uri": TOKEN_URI,
    "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url": CLIENT_X509_CERT_URL,
    "universe_domain": UNIVERSE_DOMAIN
    }

    # Convert the dictionary to JSON format
    firebase_config_json = json.dumps(firebase_config)



    # Initialize Firebase Admin SDK with the provided credentials
    cred = credentials.Certificate(json.loads(firebase_config_json))
    firebase_admin.initialize_app(cred)

    try:
        # Connect to the Firestore database
        db = firestore.client()
        print("Connected to Firestore database.")
    except Exception as e:
        print("Error connecting to Firestore database:", e)


    # INTERNAL API
    XAPIKEY=os.getenv('XAPIKEY')
    
    
    
    
    # Collections
    
    AUTH_COL='users'
    MAIN_CATEGORY_COL='main-categories'
    STORE_PROCUCTS_COL='products'
    STORAGE_COL='storage'
    MAIN_CATEGORY_COL='main-categories'
    SHOPPING_COL='shopping'
    STORE_ACTIVITIES='activities'