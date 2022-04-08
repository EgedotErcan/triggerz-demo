import docx2txt 
from pydoc import text
from tkinter import W
import boto3
import time
import urllib
import json

dosya = ""


AWS_ACCESS_KEY_ID = 'AKIAUQUQBNZUVYYCH452'
AWS_SECRET_ACCESS_KEY = '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'

job_name = 'Ertugrulllll'
    
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
                print("========== below is output of speech-to-text ========================")
                print(text) 
                print("=====================================================================")
                
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def main():
    file_uri = 's3://myexpertunity2/q2.wav'
    transcribe_file(job_name, file_uri, transcribe_client)


if __name__ == '__main__':
    main()


dosya2 = open("sesyazi.txt" ,W)
dosya2.write(dosya)
    
