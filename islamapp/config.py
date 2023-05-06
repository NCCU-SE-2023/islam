import os


class Config:
    # MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
#int(os.getenv("MONGO_PORT")) or
    # MongoDB
    MONGODB_SETTINGS: dict = {
        'db': 'islam',
        'host': os.getenv("MONGO_HOST") or "127.0.0.1",
        'port':  27017,
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))