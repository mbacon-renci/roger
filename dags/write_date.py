"A dummy DAG to just append the date and time to a data file and exit"

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from kubernetes.client import models as k8s

from roger.dag_util import default_args

with DAG(
        dag_id="write_date",
        schedule_interval="25 4 * * *",
        default_args=default_args
) as dag:
    # Volume mount definition to be shared between base and sidecar pods
    volume_mounts = [
        k8s.V1VolumeMount(
            name='dags=data',
            mount_path='/opt/airflow/dags'),
        k8s.V1VolumeMount(
            name='logs-data',
            mount_path='/opt/airflow/share/logs'),
        k8s.V1VolumeMount(
            name='airflow-data',
            mount_path='/opt/airflow/share/data'),
    ]

    # Sidecar configuration, adapted from
    # https://airflow.apache.org/docs/apache-airflow/2.5.3/core-concepts/executor/kubernetes.html
    sidecar_config = {
        "pod_override": k8s.V1PodSpec(
            containers=[
                k8s.V1Container(
                    name='base',
                    volume_mounts=volume_mounts)
                k8s.V1Container(
                    name='sidecar',
                    image='containers.renci.org/helxplatform/roger:0.10.3-dev',
                    args=["datestr=`date`; echo 'SIDECAR DATE ' $datestr >>"
                          "/opt/airflow/share/logs/sidecar_timestamp.log"],
                    command=["bash", "-cx"],
                    volume_mounts=volume_mounts)
            ]
        }

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
