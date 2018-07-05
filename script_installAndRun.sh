#!/bin/bash

clear
echo "refreshing venv/"
sudo apt-get install python3-venv
rm -r venv/
export LC_ALL=C
python3 -m venv venv/

echo "starting local API Server!"
source venv/bin/activate
pip install -r req.txt
cd src/
echo "have fun"
python manage.py runserver
