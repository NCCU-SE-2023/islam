#!/bin/bash

echo "APP_NAME: $APP_NAME, APP_ENV: $APP_ENV"

# Wait for 5 seconds
sleep 5

# Run alembic
alembic upgrade head

gunicorn -w 2 -b 0.0.0.0:5555 main:app --reload
