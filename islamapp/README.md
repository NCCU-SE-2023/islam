# ISLAM development guide

## Python env
```
python3 -m venv .ISLAMENV
source .ISLAM/bin/activate
pip3 install -r requirements.txt
```

## ISLAM database

connect to a MySQL DB (eg. localhost:3306) and create a new schema called islam

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