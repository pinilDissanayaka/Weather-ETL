from airflow import DAG
from utils import default_args
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd


with DAG(
    'Weather_DAG',
    default_args=default_args,
    description='A simple DAG used to ETL',
    schedule_interval=timedelta(days=1),
    tags=['example'],
) as dag:
    
    is_api_ready=HttpSensor(
        
    )