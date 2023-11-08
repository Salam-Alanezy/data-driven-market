import random
import datetime
from flask import session, redirect, url_for
from collections import Counter
def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(color)
    return colors

def calculate_days_to_expiry(expiry_date_str, date_format='%d.%m.%Y'):
    product_date = datetime.datetime.strptime(expiry_date_str, date_format)
    return (product_date - datetime.datetime.now()).days

def is_expiring_soon(expiry_date_str, days_threshold=7, date_format='%d.%m.%Y'):
    return calculate_days_to_expiry(expiry_date_str, date_format) <= days_threshold

def check_user_logged_in():
    return 'email' in session

def redirect_if_not_logged_in():
    if not check_user_logged_in():
        return redirect(url_for('auth.login'))

def get_expiring_products_count(products):

    expiring_products_count = {}
    for product in products:
        if product['is_expiring_soon']:
            expiring_products_count[product['name']] = expiring_products_count.get(product['name'], 0) + product['count']
    return expiring_products_count


def calculation_collection(storage_products, shopping_list):
   
    for product in storage_products:
        product['is_expiring_soon'] = is_expiring_soon(product['earliestExDate'])

    expiring_products = [p['name'] for p in storage_products if p['is_expiring_soon']]
    expiring_products_count = dict(Counter(expiring_products))
    total_products_count = len(storage_products)
    expiring_soon_count = sum(1 for product in storage_products if product['is_expiring_soon'])
    
    expiring_products_count2 = {}
    for product in storage_products:
        if product['is_expiring_soon']:
            expiring_products_count2[product['name']] = expiring_products_count2.get(product['name'], 0) + product['count']

    colors = generate_random_colors(len(expiring_products_count2))

    shopping_list_count = len(shopping_list)

    # Sorting and filtering
    expiring_products = [p for p in storage_products if p['is_expiring_soon']]
    expiring_products.sort(key=lambda x: datetime.datetime.strptime(x['earliestExDate'], '%d.%m.%Y'))
    displayed_products = set()
    filtered_expiring_products = []
    for product in expiring_products:
        if product['name'] not in displayed_products:
            displayed_products.add(product['name'])
            filtered_expiring_products.append(product)
    expiring_soon_count = len(filtered_expiring_products)
    
    return expiring_products_count2, filtered_expiring_products, expiring_soon_count, shopping_list, storage_products, total_products_count, colors,shopping_list_count
    