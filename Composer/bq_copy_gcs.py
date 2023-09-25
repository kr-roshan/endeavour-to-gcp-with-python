import csv
import datetime
import io

from airflow import models
from airflow.contrib.operators import bigquery_to_gcs
from airflow.operators import dummy_operator

default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime.today(),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

# variables
dest_bucket = "26071978-2-us"
source_table = "nyc-tlc:green.trips_2014"

with models.DAG('bq_copy_gcs',
                default_args=default_args,
                schedule_interval=None) as dag:
    start = dummy_operator.DummyOperator(
        task_id='start',
        trigger_rule='all_success'
    )

    end = dummy_operator.DummyOperator(
        task_id='end',
        trigger_rule='all_success'
    )

    BQ_to_GCS = bigquery_to_gcs.BigQueryToCloudStorageOperator(
            task_id='BQ_to_GCS',
            source_project_dataset_table=source_table,
            destination_cloud_storage_uris=['{}-*.avro'.format(
                'gs://' + dest_bucket + '/' + source_table)],
            export_format='AVRO'
        )
    
    start >> BQ_to_GCS >> end



