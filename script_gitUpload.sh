#!/bin/bash

clear
echo "uploading repository"

# 1st time only 
git init 
git remote add origin https://github.com/mymacy/django-rest-template.git


git add .
git commit -m "first commit"
git push -u origin master

echo "done"