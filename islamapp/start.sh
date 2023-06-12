#!/bin/bash

echo "APP_NAME: $APP_NAME, APP_ENV: $APP_ENV"

alembic upgrade head &
python3 -m flask run
