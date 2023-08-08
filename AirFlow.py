from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 8),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'web_scraping',
    default_args=default_args,
    description='Scrape website data once a day',
    schedule_interval=timedelta(days=1),
)

def scrape_data():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = []
    for article in soup.find_all('article'):
        titles.append(article.h3.text)

    print(titles)

scrape_task = PythonOperator(
    task_id='scrape_data',
    python_callable=scrape_data,
    dag=dag,
)