#!/bin/bash

clear
echo "making migrations..."
source venv/bin/activate
cd testserver/
python manage.py makemigrations
python manage.py migrate
echo "success!"
echo ""

echo "cleaning the static"
cd ../
rm -r static/*
echo ""

echo "collecting the static"
cd testserver/
python manage.py collectstatic