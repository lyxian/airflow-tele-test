# Airflow Scheduler

Current Build: v0

Description:

Version:

- v0 - call Carousell DAG
- v1 - call DAG to keep awake

Requirements:

- wheel (included in HEROKU)
- "apache-airflow[postgres,password]"

### Heroku Configs

- login heroku
- run .scripts/heroku/setConfig

### Set-Up Instructions

- db: heroku addons:create heroku-postgresql:hobby-dev
- web: airflow db init
- web: airflow webserver --port $PORT --daemon & airflow scheduler

### TO-DO

- create init_user script
- add python script to send request to webserver
