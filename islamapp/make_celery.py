from app import create_app
from config import Config

flask_app = create_app(config=Config)
celery_app = flask_app.extensions["celery"]