"A dummy DAG to just append the date and time to a data file and exit"

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

from roger.dag_util import default_args

with DAG(
        dag_id="write_date",
        schedule_interval="25 4 * * *",
        default_args=default_args
) as dag:

    dummy = DummyOperator(task_id="dummy_task")

    writer = BashOperator(task_id="date_writer",
                          bash_command='date >> '
                          '/opt/airflow/share/data/'
                          '_write_date_'
                          '{{ dag.dag_id }}_'
                          '{{ ti.task_id }}_'
                          '{{ ti.run_id }}'
                          )
    dummy >> writer
