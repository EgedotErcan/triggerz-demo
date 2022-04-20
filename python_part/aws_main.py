from aws_modules.aws_assign_pdf import Assign
from aws_modules.aws_comprehend import Comprehend
from aws_modules.aws_transcribe import Transcribe
import boto3
import os

class Core():
    def __init__(self,file_name):
        REGION_NAME = os.getenv("REGION_NAME")
        AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCES_KEY = os.getenv("AWS_SECRET_ACCES_KEY")
        self.s3 = boto3.client("s3",
                region_name=f"{REGION_NAME}",
                aws_access_key_id=f"{AWS_ACCESS_KEY_ID}",
                aws_secret_access_key=f"{AWS_SECRET_ACCES_KEY}")
        self.file_name = file_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.file_name)
        self.assign_object = Assign(self.file_name,Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        self.string_keywords = self.assign_object.assign_pdf()
        self.s3.upload_file('./2022_CG_Triggered_SF.pdf','myexpertunity','2022_CG_Triggered_SF.pdf',ExtraArgs={'ACL': 'public-read', 'ContentType': 'application/pdf'})
            
        


