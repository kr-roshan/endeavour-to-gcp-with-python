import datetime

from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator
from airflow.utils import trigger_rule

yesterday = datetime.datetime.combine(datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time())

default_dag_args = {
    'start_date': yesterday,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=2)
}

with models.DAG (
    'python_and_bash_with_all_success_trigger',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args) as dag:  

    def hello_world():
        raise ValueError('Oops! Something went wrong in hello world')
        print('Hello World')
        return 1
    
    def greeting():
        print('Greetings from Roshan. Happy Learning!')
        return 'Greeting successfully printed'
    
    hello_world_greeting = python_operator.PythonOperator(
        task_id='python_1',
        python_callable=hello_world)
    
    roshan_greeting = python_operator.PythonOperator(
        task_id='python_2',
        python_callable=greeting)
    
    bash_greeting = bash_operator.BashOperator(
        task_id='bash_3',
        bash_command='echo "Bye! See you soon."',
        trigger_rule=trigger_rule.TriggerRule.ALL_SUCCESS)
    
    hello_world_greeting >> roshan_greeting >> bash_greeting
    
