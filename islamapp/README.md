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
```

.flaskenv example
```
FLASK_ENV=development
FLASK_APP=main.py
FLASK_DEBUG=True
```


## Start flask
```

```


## celery

### start
```
 celery -A make_celery worker --loglevel INFO
```

## in case pip install -r requirements.txt fails
pip install flask celery flask_sqlalchemy flask_mongoengine pydantic


## quick setup db

```
docker compose up
```

.env(use docker mysql/redis/mongo)
```
FLASK_ENV=development
FLASK_APP=main.py
FLASK_DEBUG=True
DATABASE_URL="mysql://user:password@localhost:3306/database"
MONGO_HOST=127.0.0.1
MONGO_PORT=27017
```


## celery
```bash
celery -A make_celery worker --loglevel=info --logfile=logs/celery.log 
```

## flower
```bash
celery -A make_celery flower --port=5555 --broker=redis://localhost:6379
```