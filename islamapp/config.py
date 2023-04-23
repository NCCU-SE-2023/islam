import os


class Config:
    # MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # MongoDB
    MONGODB_SETTINGS: dict = {
        'db': 'islam',
        'host': os.getenv("MONGO_HOST") or "127.0.0.1",
        'port': int(os.getenv("MONGO_PORT")) or 27017,
    }
    MONGO_URI = os.getenv("MONGO_URI") or "mongodb://localhost:27017/mydatabase"
    MONGO_PORT = int(os.getenv("MONGO_PORT", "27017"))
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_TASK_IGNORE_RESULT = True