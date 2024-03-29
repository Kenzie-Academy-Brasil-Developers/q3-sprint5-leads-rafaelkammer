from flask import Flask

from app.configs import database, migration
from app import routes

def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)

    return app