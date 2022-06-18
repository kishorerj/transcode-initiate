import argparse, sys, os, time, bq
from google.cloud import logging
from google.cloud.video import transcoder_v1
from google.cloud.video.transcoder_v1.services.transcoder_service import (
    TranscoderServiceClient,
)
from google.cloud import storage


def create_bucket(bucket_name):
    client = storage.Client()
    bucket = storage.Bucket(bucket_name)
    client.create_bucket(bucket)

def create_job_from_preset( input_bucket, input_object, transcode_template, output_bucket):
    """Creates a job based on a job preset.
    Args:
        project_id: The GCP project ID.
        location: The location to start the job in.
        input_uri: Uri of the video in the Cloud Storage bucket.
        output_uri: Uri of the video output folder in the Cloud Storage bucket.
        preset: The preset template (for example, 'preset/web-hd')."""

    trancoderClient = TranscoderServiceClient()

    input_uri="gs://"+input_bucket+"/"+input_object
    output_uri="gs://"+output_bucket+"/"+input_bucket+"/"+ input_object+ "/"

    
    client = logging.Client()

    logger = client.logger("service_1")
    logger.log("Inp" + input_uri)
    logger.log("OP" + output_uri)
    
    project_id = os.environ.get('project_id')
    location = os.environ.get('location')
     
    logger.log("Project location name "+ project_id+ ","+ location)
    dataset_id=os.environ.get('dataset')
    table_id="transcoder_job_dtls"

    parent = "projects/"+project_id+"/locations/"+ location
    job = transcoder_v1.types.Job()
    job.input_uri = input_uri
    job.output_uri = output_uri
    job.template_id = transcode_template

    response = trancoderClient.create_job(parent=parent, job=job)
    print(f"Job: {response.name}")
    logger.log("Job name "+ response.name)

    bq.insert_table(project_id,dataset_id, table_id, response.name, "PROCESSING", input_uri, output_uri, job.template_id)
    return response


if( __name__ == "__main__"):
    create_job_from_preset(sys.argv[1],sys.argv[2])
