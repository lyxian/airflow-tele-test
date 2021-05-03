# Airflow Scheduler

Current Build: v0

Description:

- xx

Requirements:

- wheel (included in HEROKU)
- "apache-airflow[postgres,password]"

### Set-Up Instructions

- web: airflow db init
- web: airflow webserver --port $PORT --daemon & airflow scheduler

### TO-DO

- create init_user script
- add python script to send request to webserver
