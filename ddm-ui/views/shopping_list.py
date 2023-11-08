from flask import Blueprint, render_template, request, redirect, url_for, session
from models import get_all_shopping_products, add_product_to_shopping, update_shopping_product, delete_shopping_product

shopping_list_bp = Blueprint('shopping_list', __name__)

@shopping_list_bp.route('/shopping_list')
def shopping_list_page():

    if 'email' not in session:
        return redirect(url_for('auth.login'))

    shopping_products = get_all_shopping_products()
    shopping_list_count = len(shopping_products)
    
    return render_template('shopping_list.html', 
                           shopping_products=shopping_products,
                           shopping_list_count=shopping_list_count)


@shopping_list_bp.route('/add_to_shopping_list', methods=['POST'])
def add_to_shopping_list():

    product_data = request.form
    success = add_product_to_shopping(product_data)
    
    if success:
        return redirect(url_for('shopping_list.shopping_list_page'))
    else:
   
        return redirect(url_for('shopping_list.shopping_list_page'))


@shopping_list_bp.route('/update_shopping_product/<product_id>', methods=['POST'])
def update_shopping_product_route(product_id):

    updated_data = request.form
    success = update_shopping_product(product_id, updated_data)
    
    if success:
        return redirect(url_for('shopping_list.shopping_list_page'))
    else:
   
        return redirect(url_for('shopping_list.shopping_list_page'))


@shopping_list_bp.route('/delete_shopping_product/<product_id>', methods=['POST'])
def delete_shopping_product_route(product_id):

    success = delete_shopping_product(product_id)
    
    if success:
        return redirect(url_for('shopping_list.shopping_list_page'))
    else:
   
        return redirect(url_for('shopping_list.shopping_list_page'))
