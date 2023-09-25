from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from apis import api
from flask_cors import CORS
from config import Config

cors = CORS()

app = Flask(__name__)
cors.init_app(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api.init_app(app)

if __name__ == "__main__":
    # TODO: Consider using a production WSGI server like Gunicorn for better performance
    
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=Config.PORT)