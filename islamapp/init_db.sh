# Wait for 5 seconds
sleep 5

alembic upgrade head

cd script/dump_script
python importdata.py
