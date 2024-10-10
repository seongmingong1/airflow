import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_macro_eg1",
    schedule = "10 0 L * *",
    start_date=pendulum.datetime(2024, 10, 10, tz = 'Asia/Seoul'),
    catchup = False

) as dag:
#START Date: last day of previous month, End date: -1day
    bash_task1 = BashOperator(
        task_id ="bash_task1",
        env={'START_DATE':'{{ data_interval_start.in_timezone("Asia/Seoul") | ds }}',
            'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}'
         },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
) 