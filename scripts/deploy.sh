#!/bin/bash
# activate virtual env
source ~/venv/bin/activate
cd /var/www/JOYONWHEELS
git stash
git pull --rebase origin unit_testing
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input 
deactivate
sudo systemctl reload nginx
sudo systemctl restart gunicorn 