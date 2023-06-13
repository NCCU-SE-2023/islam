#!/bin/bash

echo "APP_NAME: $APP_NAME, APP_ENV: $APP_ENV"

# Wait for 5 seconds
sleep 5

# Run alembic
alembic upgrade head

python3 -m flask run