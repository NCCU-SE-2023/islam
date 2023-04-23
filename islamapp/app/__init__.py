from flask import Flask
from celery import Celery, Task
from api.test import test_route
from api.user import user_route
# from api.task import task_route
from database import db, mongo

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(test_route)
    app.register_blueprint(user_route)
    # app.register_blueprint(task_route)
    db.init_app(app)
    mongo.init_app(app)
 
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)

    return app