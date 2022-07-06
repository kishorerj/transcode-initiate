from google.cloud import bigquery
from datetime import datetime
import os




def insert_table(project, dataset, table, job_id, status, input_bucket_uri, output_bucket_uri, job_template):
    client = bigquery.Client()
    
    # datetime object containing current date and time
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
     
    
    errors = []
    #errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    client = bigquery.Client()
    query_text = f"""
    INSERT `{project}.{dataset}.{table}` (job_id, status, start_date, end_date, input_media_uri, output_transcoded_uri, job_template)  
    VALUES ('{job_id}', '{status}','{now}', '{now}', '{input_bucket_uri}', '{output_bucket_uri}', '{job_template}')
    """
    query_job = client.query(query_text)

    query_job.result()

if __name__ == "__main__":
    #insert_table()
    print("main hello")

