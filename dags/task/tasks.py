from airflow.providers.http.operators.http import SimpleHttpOperator
import requests

weatherAPIKey='fc78a469d8c847ac9b7996c55b895e2b'
location="portland"


weatherUrl =f"http://api.openweathermap.org/data/2.5/weather?q=portland&appid=fc78a469d8c847ac9b7996c55b895e2b&units=metric"


data=requests.get(weatherUrl).json()

print(data)
    