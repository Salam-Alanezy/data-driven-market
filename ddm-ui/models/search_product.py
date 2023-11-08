
from models import get_by_ean, get_product_by_ean
from flask import jsonify

def search_product_by_ean(ean):

    try:
        response = get_product_by_ean(ean=ean) 
        print(response)
    
        if response.status_code == 200:
            return response
        else:
    
            secondResponse = get_by_ean(ean=ean)
            
            if secondResponse.status_code == 200:
                return secondResponse
            else:
                return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        print(e)