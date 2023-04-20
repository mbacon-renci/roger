"A dummy DAG to just append the date and time to a data file and exit"

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

with DAG(
        dag_id="write_date",
        schedule_interval="25 4 * * *",
) as dag:

    dummy = DummyOperator("Initial task")

    writer = BashOperator(task_id="date_writer",
                          bash_command='date >> '
                          '/opt/airflow/share/data')
    dummy >> writer
