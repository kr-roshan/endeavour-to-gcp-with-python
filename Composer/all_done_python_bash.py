# all done trigger: All directly upstream tasks are done. The status of this task is not taken into account. 
# For example, this is useful to trigger downstream tasks that do not need any result, only timing.

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
    'python_and_bash_with_all_done_trigger',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args) as dag:  

    def hello_world():
        raise ValueError('Oops! Something went wrong in hello world')
        print('Hello World')
        return 1
    
    def greeting():
        raise TypeError('Incorrect type in greeting.') # this is optional
        print('Greetings from Roshan. Happy Learning!')
        return 'Greeting successfully printed'
    
    hello_world_greeting = python_operator.PythonOperator(
        task_id='python_hello_world',
        python_callable=hello_world)
    
    roshan_greeting = python_operator.PythonOperator(
        task_id='python_roshan_greeting',
        python_callable=greeting)
    
    bash_greeting = bash_operator.BashOperator(
        task_id='bash_greeting',
        bash_command='echo "Bye! See you soon."',
        trigger_rule=trigger_rule.TriggerRule.ALL_DONE)
    
    hello_world_greeting >> roshan_greeting >> bash_greeting
    
