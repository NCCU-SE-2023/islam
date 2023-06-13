#!/bin/bash

echo "APP_NAME: $APP_NAME, APP_ENV: $APP_ENV"

# Call init_db.sh script
./init_db.sh

# Start gunicorn
gunicorn -w 2 -b 0.0.0.0:5555 main:app --reload
