# Weather Data ELT Pipeline with Apache Airflow

This repository contains an ELT (Extract, Load, Transform) pipeline built using Apache Airflow, AWS EC2, and AWS S3 for collecting, storing, and transforming weather data from various sources. The pipeline is designed to be modular, scalable, and easy to customize for different weather data APIs and storage backends.

## Features

1. Automated Data Extraction: Fetches weather data from APIs such as OpenWeatherMap, WeatherAPI, or NOAA.

2. Flexible Data Storage: Stores raw data in AWS S3 and supports further storage in databases like PostgreSQL or MySQL.

3. Data Transformation: Cleans and transforms raw data for analytical use.

4. Scheduling and Monitoring: Leverages Apache Airflow for task orchestration, monitoring, and logging.

5. Extensible Design: Easily adapt the pipeline for new data sources or additional processing steps.

## Pipeline Overview

1. The ELT process consists of the following stages:

2. Extract: Pulls raw weather data from the API.

3. Transform: Processes and formats the data for downstream analysis.

4. Load: Stores the raw data in AWS S3 as a staging area.

![Screenshot from 2024-12-11 08-27-35](https://github.com/user-attachments/assets/0770d72a-d061-4355-b6de-85a9e54f91e7)


  
## Getting Started

### Prerequisites

1. Python 3.8+

2. Apache Airflow 2.0+

3. AWS Account: For EC2 instances and S3 storage.

4. Database: PostgreSQL, MySQL, or another compatible database (optional).

5. Weather API Key: Obtain an API key from your chosen weather data provider.

### Installation

1. Clone the repository:
```
git clone https://github.com/pinilDissanayaka/Weather-ETL.git
cd Weather-ETL.git
```

2. Set up a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Configure Airflow:
```
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

5. Set environment variables for the Weather API and AWS:

```
export WEATHER_API_KEY=<your_api_key>
export WEATHER_API_URL=<api_endpoint>
export AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
export S3_BUCKET_NAME=<your_s3_bucket_name>
```

Start the Airflow scheduler and web server:

```
airflow atandalone
```

