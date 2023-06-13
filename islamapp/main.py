from app import create_app
from config import Config

app = create_app(config=Config)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
