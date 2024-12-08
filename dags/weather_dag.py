from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd




def kelvin_to_fahrenheit(temp_in_kelvin):
    temp_in_fahrenheit = (temp_in_kelvin - 273.15) * (9/5) + 32
    return temp_in_fahrenheit


def transform_load_data(task_instance):
    data = task_instance.xcom_pull(task_ids='extract_weather_data')



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 8),
    'email': ['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}



with DAG('weather_dag',
        default_args=default_args,
        schedule_interval = '@daily',
        catchup=False) as dag:


        is_weather_api_ready = HttpSensor(
            task_id ='is_weather_api_ready',
            http_conn_id='weathermap_api',
            endpoint="/data/2.5/weather?q=portland&appid=fc78a469d8c847ac9b7996c55b895e2b&units=metric"
        )


        extract_weather_data = SimpleHttpOperator(
            task_id = 'extract_weather_data',
            http_conn_id = 'weathermap_api',
            endpoint="/data/2.5/weather?q=portland&appid=fc78a469d8c847ac9b7996c55b895e2b&units=metric",
            method = 'GET',
            response_filter= lambda r: json.loads(r.text),
            log_response=True
        )

        transform_weather_data = PythonOperator(
            task_id= 'transform_load_weather_data',
            python_callable=transform_load_data
        )




        is_weather_api_ready >> extract_weather_data >> transform_weather_data