from flask import Flask
from api.test import test_route
from api.user import user_route
from api.task import task_route
from api.query import query_route
from database import db, mongo


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(test_route)
    app.register_blueprint(user_route)
    app.register_blueprint(task_route)
    app.register_blueprint(query_route)
    db.init_app(app)
    mongo.init_app(app)
    return app
