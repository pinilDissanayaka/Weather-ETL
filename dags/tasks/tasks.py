from airflow.providers.http.sensors.http import HttpSensor


city_name = "London"
API_KEY="fc78a469dfc78a469d8c847ac9b7996c55b895e2b"

is_api_ready=HttpSensor(
        task_id="is_api_is_ready",
        http_conn_id="weather_api",
        endpoint=f"/data/2.5/weather?q={city_name}&appid={API_KEY}"
)