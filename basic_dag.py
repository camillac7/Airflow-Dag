from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Default arguments that will be applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'basic_dag',
    default_args=default_args,
    description='A very basic DAG example',
    schedule=timedelta(days=1),  # Run daily (Airflow 3.x uses 'schedule' instead of 'schedule_interval')
    start_date=datetime(2024, 1, 1),
    catchup=False,  # Don't backfill past runs
    tags=['example', 'basic'],
)

# Define a simple Python function
def print_hello():
    print("Hello from Airflow!")
    return "Hello World"

# Task 1: Bash operator
task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task 2: Python operator
task2 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Task 3: Another bash operator
task3 = BashOperator(
    task_id='print_goodbye',
    bash_command='echo "Goodbye from Airflow!"',
    dag=dag,
)

# Define task dependencies
# task1 runs first, then task2 and task3 run in parallel
task1 >> task2
task1 >> task3

