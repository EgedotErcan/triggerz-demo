from aws_modules.aws_assign_pdf import Assign
from aws_modules.aws_comprehend import Comprehend
from aws_modules.aws_transcribe import Transcribe
import boto3

class Core():
    def __init__(self,file_name):
        self.s3 = boto3.client("s3",
                region_name="us-east-1",
                aws_access_key_id="AKIAUQUQBNZUWY4J4ZJR",
                aws_secret_access_key="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")
        self.file_name = file_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.file_name)
        self.assign_object = Assign(self.file_name,Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        self.string_keywords = self.assign_object.assign_pdf()
        self.s3.upload_file('./2022_CG_Triggered_SF.pdf','myexpertunity','2022_CG_Triggered_SF.pdf',ExtraArgs={'ACL': 'public-read', 'ContentType': 'application/pdf'})
            
        


