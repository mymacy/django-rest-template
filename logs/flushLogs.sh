#!/bin/bash

clear
echo "Hi, $USER!"

echo "creating backup in /bckp"
cp ./gunicorn.access.log ./bckp/gunicorn.access.log
cp ./gunicorn.error.log ./bckp/gunicorn.error.log
cp ./nginx-access.log ./bckp/nginx-access.log
cp ./nginx-error.log ./bckp/nginx-error.log
cp ./supervisor.err.log ./bckp/supervisor.err.log
cp ./supervisor.out.log ./bckp/supervisor.out.log

echo "clearing logs..."
:> gunicorn.access.log
:> gunicorn.error.log
:> nginx-access.log
:> nginx-error.log
:> supervisor.err.log
:> supervisor.out.log
