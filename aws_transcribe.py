import boto3
import time
import urllib
import json


current_client = "ertugrul"
current_waw_file_name = "q1"
job_name = current_client
   
transcribe_client = boto3.client('transcribe', aws_access_key_id="AKIAUQUQBNZUVYYCH452", aws_secret_access_key="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", region_name='us-east-1')

def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )
    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']
                print(text) 
                
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(4)


def main(current_waw_file_name):

    file_uri = f's3://myexpertunity/{current_waw_file_name}.wav'
    transcribe_file(job_name, file_uri, transcribe_client)


if __name__ == '__main__':
    main(current_waw_file_name)


