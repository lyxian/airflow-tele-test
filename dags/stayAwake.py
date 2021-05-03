import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Py.main import getDateNow, live
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

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
    dag_id='stay_awake',
    default_args=default_args,
    schedule_interval='*/10 * * * *',
    catchup=False,
)

t1 = PythonOperator(
    task_id='live',
    python_callable=live,
    dag=dag,
    #op_args=,
    #op_kwargs=kwargs,
)

t1