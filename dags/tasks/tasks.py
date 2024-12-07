from airflow.providers.http.sensors.http import HttpSensor
import os



city_name="london"
API_KEY="fc78a469dfc78a469d8c847ac9b7996c55b895e2b"


weather_end_point=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"


is_api_is_ready=HttpSensor()