from flask import Flask
from api.test import test_route
from api.user import user_route
from database import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(test_route)
    app.register_blueprint(user_route)
    db.init_app(app)
    return app