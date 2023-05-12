import os
import dotenv

dotenv.load_dotenv()

class Config:
    # MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # MongoDB
    MONGODB_SETTINGS: dict = {
        'db': os.getenv("MONGO_DB") or "islam",
        'host': os.getenv("MONGO_HOST") or "127.0.0.1",
        'port': int(os.getenv("MONGO_PORT")) or 27017,
        'username': 'islam',
        'password': 'islam',
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))