from datetime import datetime
import random
import requests
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def print_random_number_squared():
    random_number = random.randint(1, 100)
    print(random_number ** 2)


def get_weather(location):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        print('Success')
    else:
        print('Failure')


with DAG(
    "homework_6_dag",
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    random_number_bash = BashOperator(
        task_id="random_bash",
        bash_command="echo $RANDOM"
    )

    random_number_python = PythonOperator(
        task_id="random_python",
        python_callable=print_random_number_squared
    )

    weather_api_call = PythonOperator(
        task_id="weather_api_call",
        python_callable=get_weather,
        op_kwargs={"location": "Moscow"}
    )

random_number_bash >> random_number_python >> weather_api_call
