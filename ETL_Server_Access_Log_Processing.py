# Import the libraries

from datetime import timedelta
from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# defining the dag arguments
default_args = {
    'owner': 'Raphael Malims',
    'start_date': days_ago(0),
    'email': ['raphaelmalims@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries':1,
    'retry_delay':timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='My first DAG',
    schedule=timedelta(days=1),
)


# defining the tasks.
# define the task 'download'
download = BashOperator(
    task_id='download',
    bash_command='wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt" -O ~/Zen/Airflow-ETL-S.A.L.P/web-server-access-log.txt',
    dag=dag,
)

#defining the task 'extract'
extract = BashOperator(
    task_id='extract',
    bash_command='cut -f1,4 -d"#" ~/Zen/Airflow-ETL-S.A.L.P/web-server-access-log.txt > ~/Zen/Airflow-ETL-S.A.L.P/extracted.txt',
    dag=dag,
)

# 'Transform' task.
transform = BashOperator(
    task_id='transform',
    bash_command='tr "[a-z]" "[A-Z]" < ~/Zen/Airflow-ETL-S.A.L.P/extracted.txt > ~/Zen/Airflow-ETL-S.A.L.P/capitalized.txt',
    dag=dag,
)

# 'Load' Task.
load = BashOperator(
    task_id='load',
    bash_command='zip log.zip ~/Zen/Airflow-ETL-S.A.L.P/capitalized.txt',
    dag=dag,
)

# task pipeline
download >> extract >> transform >> load
