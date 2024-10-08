import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator_template", 
    schedule="10 0 * * *", 
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"),
    catchup=False, 

) as dag:
    
    bash_t1 = BashOperator(  
        task_id="bash_t1",  
        bash_command='echo "data_interval_end: {{ data_interval_end }}"'
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        env={
            'START_DATE': '{{ data_interval_start | ds }}', #key value 설정. 딕셔너리 타입으로. 
            'END_DATE': '{{ data_interval_end | ds }}'},
        bash_command ='echo $START_DATE && $END_DATE' # && 앞에게 성공하면 뒤에 것도 실행하겠다는 뜻.
                       
    )

    bash_t1 >> bash_t2