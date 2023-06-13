import os
import dotenv

dotenv.load_dotenv()


class Config:
    # MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:islam@127.0.0.1:3306/islam"
    )

    # MongoDB
    MONGODB_SETTINGS: dict = {
        "db": os.getenv("MONGO_DB", "islam"),
        "host": os.getenv("MONGO_HOST", "127.0.0.1"),
        "port": int(os.getenv("MONGO_PORT", "27017")),
        "username": "islam",
        "password": "islam",
    }
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
