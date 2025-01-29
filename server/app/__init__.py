from flask import Flask
from flask_cors import CORS
import os

# In development mode
if os.getenv("DB_URL") == None:
    from dotenv import load_dotenv

    load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from .routes import api

    app.register_blueprint(api)

    return app
