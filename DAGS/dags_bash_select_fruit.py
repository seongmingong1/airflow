from airflow import DAG
import pendulum
import datetime
from airflow.operators.empty import BashOperator


with DAG(
    dag_id = "dags_bash_select_fruit", 
    schedule="10 0 * * 6#1", #every first saturday 0hour 10min
    start_date=pendulum.datetime(2024,3,1,tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    t1_Orange =BashOperator(
        task_id="t1_Orange", 
        bash_command = "opt/airflow/plugins/shell/select_fruit.sh ORANGE",

    )

    t2_avocado =BashOperator(
        task_id="t2_avocado", 
        bash_command = "opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
        
    )
    

t1_Orange >> t2_avocado