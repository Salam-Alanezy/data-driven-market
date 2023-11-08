from flask import Blueprint, render_template, session, redirect, url_for
from views.utils import calculation_collection
from models.storage_product import get_all_products
from models.shopping_product import get_all_shopping_products

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def index():
    if 'email' not in session:
        return redirect(url_for('auth.login'))

    
    storage_products = get_all_products()
    shopping = get_all_shopping_products()
    expiring_products_count2, filtered_expiring_products, expiring_soon_count, shopping_list, storage_products, total_products_count, colors,shopping_list_count = calculation_collection(storage_products, shopping)

    return render_template(
        'dashboard.html',
        expiring_products_count2=expiring_products_count2,
        expiring_products=filtered_expiring_products,
        expiring_soon_count=expiring_soon_count,
        shopping_list=shopping_list,
        products=storage_products,
        total_products_count=total_products_count,
        colors=colors,
        shopping_list_count=shopping_list_count
    )
