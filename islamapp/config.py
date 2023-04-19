import os


class Config:
    # MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # MongoDB
    MONGODB_SETTINGS: dict = {
        'db': 'islam',
        'host': 'localhost',
        'port': 27017
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))