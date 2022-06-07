from google.cloud import bigquery
from datetime import datetime
import os

def update_table(project, dataset, table, job_id, status, input_bucket_uri, output_bucket_uri, job_template):
    project_id= os.environ.get('project')
    dataset_id= os.environ.get('dataset')
    table_id="trancoder_job_dtls"
    table_id = project+ "." + dataset + "." + table
    client = bigquery.Client()
    query_text = f"""
    UPDATE `{project_id}.{dataset_id}.{table_id}`
    SET status = "FAILED"
    WHERE job_id="Phred Phlyntstone"
    """
    query_job = client.query(query_text)

    # Wait for query job to finish.
    query_job.result()


def insert_table(project, dataset, table, job_id, status, input_bucket_uri, output_bucket_uri, job_template):
    client = bigquery.Client()
    table_id = "kishorerjbloom.test_sample.trancoder_job_dtls"
    # datetime object containing current date and time
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
     
    
    errors = []
    #errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    client = bigquery.Client()
    query_text = f"""
    INSERT {project}.{dataset}.{table} (job_id, status, start_date, end_date, input_media_uri, output_transcoded_uri, job_template)  
    VALUES ('{job_id}', '{status}','{now}', '{now}', '{input_bucket_uri}', '{output_bucket_uri}', '{job_template}')
    """
    query_job = client.query(query_text)

    query_job.result()

if __name__ == "__main__":
    #insert_table()
    print("main hello")

