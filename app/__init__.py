from flask import Flask
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    CORS(app)

    from app.controllers import user_bp

    app.register_blueprint(user_bp)
    return app