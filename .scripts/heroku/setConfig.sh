#!/bin/bash

# Create workflow to check if logged in

# Initialize Airflow variable
var=AIRFLOW__CORE__SQL_ALCHEMY_CONN
if [[ $(heroku config:set $var=$(heroku config:get DATABASE_URL)) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi

var=AIRFLOW__CORE__LOAD_EXAMPLES
if [[ $(heroku config:set $var=False) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi

var=AIRFLOW_HOME
if [[ $(heroku config:set $var=/app) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi

var=AIRFLOW__CORE__FERNET_KEY
if [[ $(heroku config:set $var=$(python $(dirname $0)/fernetKey.py)) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi

##
var=AIRFLOW__WEBSERVER__AUTHENTICATE
val=True
if [[ $(heroku config:set $var=$val) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi

var=AIRFLOW__WEBSERVER__AUTH_BACKEND
val=airflow.contrib.auth.backends.password_auth
if [[ $(heroku config:set $var=$val) ]]
then
echo "Sucess...$var set"
else
echo "Error...$var not set"
fi