from collections import Counter
import datetime
from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
from models import get_all_products, search_product_by_ean, add_product_to_storage, get_all_shopping_products, update_product_in_storage, delete_product_from_storage
from views.utils import calculation_collection
import json

products_bp = Blueprint('products', __name__)



storage = get_all_products()
shopping = get_all_shopping_products()
expiring_products_count, filtered_expiring_products, expiring_soon_count, shopping_list, storage_products, total_products_count, colors,shopping_list_count = calculation_collection(storage, shopping)
@products_bp.route('/products-page')
def products_page():
    # Sjekk om brukeren er logget inn
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template(
        'products.html', 
        expiring_products_count=expiring_products_count,
        expiring_products=filtered_expiring_products,
        expiring_soon_count=expiring_soon_count,
        shopping_list=shopping_list,
        products=storage_products,
        total_products_count=total_products_count,
        colors=colors,
        shopping_list_count=shopping_list_count
    )

@products_bp.route('/product-counting',  methods=['GET'])
def product_counting():
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('product_counting.html',expiring_products_count2=expiring_products_count, expiring_products=filtered_expiring_products, 
                           expiring_soon_count=expiring_soon_count,  products=storage_products, total_products_count=total_products_count, colors=colors, shopping_list_count=shopping_list_count)

@products_bp.route('/add-product', methods=['POST'])
def add_product():

    product_data = request.form
   
    success = add_product_to_storage(product_data)
    
    if success:
        return redirect(url_for('products.products_page'))
    else:
   
        return redirect(url_for('products.products_page'))

@products_bp.route('/get-storage', methods=['GET'])
def get_storage():
    if 'email' not in session:
        return redirect(url_for('auth.login'))
  
    
    
    products_list = []
    for product in storage:
        row = product['id']
        product['id'] = row 
        product['image'] = product['image']
        product_date = datetime.datetime.strptime(product['earliestExDate'], '%d.%m.%Y')
        days_to_expiry = (product_date - datetime.datetime.now()).days
        product['is_expiring_soon'] = days_to_expiry <= 7
        products_list.append(product)

    return jsonify(products_list)

@products_bp.route('/update-storage-products', methods=['PUT'])
def update_storage_products():
    data = request.get_json()

    # Sjekk om 'image' -feltet er tilstede i JSON-dataene
    if 'image' not in data:
        return jsonify({'status': 'error', 'message': 'Image data is missing'}), 400

    count_str = data['count'].replace('stk.', '').strip()
    count = int(count_str)

    price_str = data['price'].replace(',-', '').strip()
    price = int(price_str)

    payload = json.dumps({
        "ean": data['ean'],
        "name": data['name'],
        "brand": data['brand'],
        "count": int(count_str),
        "earliestExDate": data['earliestExDate'],
        "price": int(price_str),
        "status": False,
        "image": data['image']
    })

    response = update_product_in_storage(data['id'], payload)
    if response.status_code != 200:
        return jsonify({'status': 'error', 'message': 'Failed to save product data'}), 400

    return jsonify({'status': 'success', 'message': 'Product data saved successfully'}), 200

 
@products_bp.route('/delete-product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    
    success = delete_product_from_storage(product_id)
    
    if success:
        return redirect(url_for('products.products_page'))
    else:
   
        return redirect(url_for('products.products_page'))


@products_bp.route('/product/<ean>', methods=['GET', 'POST'])
def get_product(ean):
    if 'email' not in session:
        return redirect(url_for('auth.login'))

    response = search_product_by_ean(ean=ean)
    return jsonify(response.json())
