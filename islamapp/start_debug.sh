#!/bin/bash

echo "APP_NAME: $APP_NAME, APP_ENV: $APP_ENV"

./init_db.sh

python3 -m flask run
