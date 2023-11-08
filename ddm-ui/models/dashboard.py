import datetime
from collections import Counter
from config import Config
import requests
from flask import jsonify
import json 
from api_handler import APIHandler as api
products = []
def products_calculations():
    raw_products = api.get_ddma(endpoint='/v1/storage/get-all')
   
 
    for product in raw_products:
        product_date = datetime.datetime.strptime(product['earliestExDate'], '%d.%m.%Y')
        days_to_expiry = (product_date - datetime.datetime.now()).days
        product['is_expiring_soon'] = days_to_expiry <= 7
        products.append(product)

    # Count the products that are expiring soon
    expiring_products = [p['name'] for p in products if p['is_expiring_soon']]
    expiring_products_count = dict(Counter(expiring_products))
    total_products_count = len(products)
    expiring_soon_count = sum(1 for product in products if product['is_expiring_soon'])

    shopping_list = api.get_ddma(endpoint='/v1/shopping/get-all')
        
    return shopping_list, products, total_products_count, expiring_soon_count, expiring_products_count
        
        
def get_storage_products():
    return api.get_ddma(endpoint='/v1/storage/get-all')

def get_shopping_list():
    return api.get_ddma(endpoint='/v1/shopping/get-all')

def get_products_by_ean(ean):
    response = api.get_kassal(ean=ean)
    if response['status'] == 200:
        return jsonify(response)
    else:
        secondResponse = api.get_ddma(f"/v1/store/getProductByEAN/{ean}")
        try:
            return jsonify(secondResponse)
        except:
            return jsonify({"error": "Product not found"}), 404


def save_products_to_storage(product):
    payload = json.dumps({
        "ean": product['ean'],
        "uid": Config.UID,  # Make sure Config.UID is imported or defined here
        "earliestExDate": product['earliestExDate'],
        "price": product['price'],
        "brand": product['brand'],
        "name": product['name'],
        "count": product['count']
    })
    response = api.add_ddma('/v1/storage/add-item', payload=payload)
    return response