from flask import Flask

# Importere blueprints fra de forskjellige view-modulene
from .auth import auth
from .dashboard import dashboard
from .storage_products import products_bp
from .shopping_list import shopping_list_bp
from .planing import planing
def init_app(app: Flask):

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(shopping_list_bp, url_prefix='/shopping_list')
    app.register_blueprint(planing, url_prefix='/planing')
