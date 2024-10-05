from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_email_operator", 
    schedule="* 8 1 * *", #every month 1st 8 o'clock
    start_date=pendulum.datetime(2024,3,1,tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'ars.tretyakov@gmail.com',
        subject= 'Airflow project',
        html_content= 'I made auto mail sending system with Airflow <br> molodech'
         
    )