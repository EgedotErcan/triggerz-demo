import boto3
import time
import urllib
import json

class Transcribe():

    def __init__(self,file_url,job_name):
        self.file_url = file_url
        self.job_name = job_name
        self.transcribe_client = boto3.client('transcribe',
                                aws_access_key_id="AKIAUQUQBNZUWY4J4ZJR",
                                aws_secret_access_key="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",
                                region_name='us-east-1')

    def transcribe_file(self):
        self.transcribe_client.start_transcription_job(
            TranscriptionJobName=str(self.job_name),
            Media={'MediaFileUri': f"s3://myexpertunity/{self.file_url}.wav"},
            MediaFormat='wav',
            LanguageCode='en-US'
        )
        max_tries = 60
        while max_tries > 0:
            max_tries -= 1
            job = self.transcribe_client.get_transcription_job(TranscriptionJobName=str(self.job_name))
            job_status = job['TranscriptionJob']['TranscriptionJobStatus']
            if job_status in ['COMPLETED', 'FAILED']:
                print(f"Job {self.job_name} is {job_status}.")
                if job_status == 'COMPLETED':
                    response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                    data = json.loads(response.read())
                    text = data['results']['transcripts'][0]['transcript']
                    return text
                break
            else:
                print(f"Waiting for {self.job_name}. Current status is {job_status}.")
            time.sleep(10)