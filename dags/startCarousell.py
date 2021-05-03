import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Py.main import getDateNow, start
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

default_args = {
    'owner': 'Lyx',
    'depends_on_past': False,
    'start_date': getDateNow(),
    # 'concurrency': 1,
    'email': ['lyxlyxi@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    dag_id='start_carousell',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False,
)

t1 = PythonOperator(
    task_id='start',
    python_callable=start,
    dag=dag,
    #op_args=,
    #op_kwargs=kwargs,
)

t1