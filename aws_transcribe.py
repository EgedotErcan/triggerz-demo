import boto3
import time
import urllib
import json
import pandas as pd

transcribe_client = boto3.client('transcribe',
                                aws_access_key_id="AKIAUQUQBNZUWY4J4ZJR",
                                aws_secret_access_key="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",
                                region_name='us-east-1')
comprehend = boto3.client('comprehend', 
                        region_name = 'us-east-1',
                        aws_access_key_id = "AKIAUQUQBNZUWY4J4ZJR",
                        aws_secret_access_key = "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")
s3 = boto3.client("s3",
                region_name="us-east-1",
                aws_access_key_id="AKIAUQUQBNZUWY4J4ZJR",
                aws_secret_access_key="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")

def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=str(job_name),
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )
    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=str(job_name))
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                global text
                text = data['results']['transcripts'][0]['transcript']
                
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)

def txt_to_s3(current_txt_file_name):
    with open("q"+str(current_txt_file_name)+".txt","w") as txt:
        txt.write(text)   
    time.sleep(2)
    s3.upload_file(f'./q{str(current_txt_file_name)}.txt','myexpertunity',f'q{str(current_txt_file_name)}.txt',ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/plain'})   

def read_txt_to_comp(current_txt_file_name):
    with open("q"+str(current_txt_file_name)+".txt","r") as txt:
        data_string = txt.read()
        return [data_string]

def extract_key_phrase(dump):
    key_phrases_batch_output = comprehend.batch_detect_key_phrases(TextList=dump, LanguageCode='en')
    df = pd.DataFrame(key_phrases_batch_output['ResultList'][0]['KeyPhrases'])
    print(df.to_string())

def main(current_waw_file_name):

    file_uri = f's3://myexpertunity/q{str(current_waw_file_name)}.wav'
    transcribe_file(current_waw_file_name, file_uri, transcribe_client)


if __name__ == '__main__':

    for id , txt_id in zip(range(1,3),range(1,3)):
        main(id)
        txt_to_s3(txt_id)
        extract_key_phrase(read_txt_to_comp(txt_id))
    
     
        
    
        
        
  





