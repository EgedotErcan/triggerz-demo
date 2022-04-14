from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas as pd
import numpy as np
import textwrap
import boto3
import time
import urllib
import json

class Core():
    def __init__(self,file_name):
        self.file_name = file_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.file_name)
        self.assign_object = Assign(self.file_name,Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        self.string_keywords = self.assign_object.assign_pdf()

class Comprehend():
    
    def __init__(self,string_data):
        self.data = [string_data]
        self.comprehend = boto3.client('comprehend', 
                        region_name = 'us-east-1',
                        aws_access_key_id = "AKIAUQUQBNZUWY4J4ZJR",
                        aws_secret_access_key = "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")
    
    def comprehend_file(self):
        data_output = self.comprehend.batch_detect_key_phrases(TextList=self.data, LanguageCode='en')
        return data_output


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
                    self.delete_transcribe_object()
                    return text
                break
            else:
                print(f"Waiting for {self.job_name}. Current status is {job_status}.")
            time.sleep(10)
        
    def delete_transcribe_object(self):
        self.transcribe_client.delete_transcription_job(TranscriptionJobName=f"{self.job_name}")
        

class Assign():
    def __init__(self,file_name,keywords):
        self.file_name = file_name
        self.keywords = keywords
        self.target_file = "python_part/2022_CG_Triggered_SF_processed.pdf"
        self.original_file = "python_part/2022_CG_Triggered_SF_template.pdf"  
        self.data_preprocessing()

    def assign_pdf(self):
        packet = io.BytesIO()
        my_canvas = canvas.Canvas(packet, pagesize=letter)
        match self.file_name:
            case "q1":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,617)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q2":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,557)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q3":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,500)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q4":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,440)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q5":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,377)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q6":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,303)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q7":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,241)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q8":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,182)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case "q9":
                textobject = my_canvas.beginText()
                textobject.setTextOrigin(130,137)
                textobject.setFont("Helvetica", 8)
                wrapped_text = "\n".join(textwrap.wrap(self.keywords,110))
                textobject.textLines(wrapped_text)
                my_canvas.drawText(textobject)
            case _:
                print("Not founded")
        my_canvas.save()
        packet.seek(0)
        retention_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open(self.original_file, "rb"))
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(retention_pdf.getPage(0))
        output.addPage(page)
        outputStream = open(self.target_file, "ab")
        output.write(outputStream)
        outputStream.close()
        return self.keywords

    def data_preprocessing(self):
        string_keywords_array = pd.DataFrame(self.keywords)["Text"].to_numpy(dtype="str")
        string_keywords_str = ",".join(string_keywords_array)
        self.keywords = string_keywords_str


Core("q5")





