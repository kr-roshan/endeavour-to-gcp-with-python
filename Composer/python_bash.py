import datetime

from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator

yesterday = datetime.datetime.combine(datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time())

default_dag_args = {
    'start_date': yesterday
}

with models.DAG (
        'running_python_and_bash_operator', 
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:

    def HelloWorld():
        print("Hello World")
        return 1

    def Greeting():
        print("Greetings from Roshan! Happy coding")
        return 'Greeting successfully printed'

    hello_world_greeting = python_operator.PythonOperator(
        task_id='Python_1',
        python_callable=HelloWorld
    )

    rk_greeting = python_operator.PythonOperator(
        task_id='Python_2',
        python_callable=Greeting
    )

    bash_greeting = bash_operator.BashOperator(
        task_id='bye_bash',
        bash_command='echo "Hello World"'
    )        

    hello_world_greeting >> rk_greeting >> bash_greeting

    