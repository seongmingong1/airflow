import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", #Dag 이름들 id, 보통 Py파일명과 일치시키는 것이 좋음. 
    schedule="0 0 * * *", #분, 시, 일, 월, 요일 0시 0분 매일 돈다고 되어있음. 
    start_date=pendulum.datetime(2024, 3, 1, tz="Asis/Seoul"), #언제부터 돌 건지 설정 tz=타임존 Asis/Seoul 로 설정
    catchup=False, #False 로 되어 있으면 시작된 날짜로 부터 시작된 날짜 사이에 누락 데이터 안 돌림, True는 누락 데이터 다 돌림. 
    #dagrun_timeout=datetime.timedelta(minutes=60),  
    #tags=["example", "example2"],
    #params={"example_key": "example_value"},
) as dag:
    
    bash_t1 = BashOperator(  # 객체명
        task_id="bash_t1", #객체명과 task id 도 통일하는게 좋음. 
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command ="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2