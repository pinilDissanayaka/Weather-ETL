from airflow import DAG
from utils import default_args
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd


city_name = "London"
API_KEY="fc78a469dfc78a469d8c847ac9b7996c55b895e2b"


def load_data(task_instance):
    data=task_instance.xcom_pull(task_ids="extract_data")
    print(data)


with DAG(
    'Weather_DAG',
    default_args=default_args,
    description='A simple DAG used to ETL',
    schedule_interval=timedelta(days=1),
    tags=['example'],
    catchup=False
) as dag:
    
    is_api_ready = HttpSensor(
        task_id ='is_api_is_ready',
        http_conn_id='weather_api',
        endpoint='/data/2.5/weather?q=Portland&APPID=fc78a469dfc78a469d8c847ac9b7996c55b895e2b'
        )
    
    
    extract_data=SimpleHttpOperator(
        task_id="extract_data",
        http_conn_id="weather_api",
        endpoint=f"/data/2.5/weather?q={city_name}&appid={API_KEY}",
        method="GET",
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )
    
    load_extracked_data=PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )
    
    is_api_ready >> extract_data >> load_extracked_data