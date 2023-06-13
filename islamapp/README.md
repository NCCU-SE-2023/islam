# ISLAM development guide

## Python env
```
python3 -m venv .ISLAMENV
source .ISLAM/bin/activate
pip3 install -r requirements.txt
```

## ISLAM database

connect to a MySQL DB (eg. localhost:3306) and create a new schema called islam
connect to a Mongo DB (eg. localhost:27017) and create a new database called islam

### Alembic
set environment variable for DB connection
```
export DATABASE_URL="mysql+pymysql://{username}:{password}@{db_fqdn}:3306/islam"
```

auto generate new alembic version file after you change db data in shyguyapp/model/
```
alembic revision --autogenerate -m "modification message"
```

update DB to latest alembic version
```
alembic upgrade head
```

## Add .env and .flaskenv

.env example
```
DATABASE_URL=mysql+pymysql://{username}:{password}@{db_fqdn}:3306/islam
MONGO_HOST=127.0.0.1
MONGO_PORT=27017
MONGODB=islam
MONGO_USER=islam
MONGO_PASSWORD=islam
SELENIUM_GRID_HUB_ENDPOINT=http://localhost:4444/wd/hub
SELENIUM_GRID_GRAPHQL_END_POINT=http://localhost:4444/graphql
```

.flaskenv example
```
FLASK_ENV=development
FLASK_APP=main.py
FLASK_DEBUG=True
```


## Start flask
```
python3 -m flask run
```
## Start gunicorn
```
gunicorn -w 4 -b 127.0.0.1:5000 main:app --reload
```


## Start Scraper Controller
```
python3 run_scraper_controller.py

# To track scraper controller
tail -f logs/mission.log
tail -f logs/status.log
```
