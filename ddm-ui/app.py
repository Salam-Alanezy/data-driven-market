from flask import Flask, session, redirect, url_for
from config import Config
from views.auth import auth
from views.dashboard import dashboard
from views.storage_products import products_bp
from views.shopping_list import shopping_list_bp
from views.planing import planing

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

def unique_filter(dicts, key_name):
    seen = set()
    unique_dicts = []
    for d in dicts:
        if d[key_name] not in seen:
            seen.add(d[key_name])
            unique_dicts.append(d)
    return unique_dicts

app.jinja_env.filters['unique'] = unique_filter


# Register blueprints without url_prefix
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(products_bp)
app.register_blueprint(shopping_list_bp)
app.register_blueprint(planing)
@app.route('/')
def index():
    # Check if user is not logged in, and redirect to login page
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    # Otherwise, redirect to dashboard page
    return redirect(url_for('dashboard.index'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run('0.0.0.0', Config.PORT, debug=True)
