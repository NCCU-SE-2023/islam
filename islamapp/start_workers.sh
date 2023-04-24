#!/bin/bash
export MONGO_PORT=27017
export DATABASE_URL="mysql://user:password@localhost:3306/database"

for i in {1..5} # start 5 workers
do
    celery -A make_celery worker -n "worker$i" --loglevel=info --logfile="logs/worker$i.log" &
done