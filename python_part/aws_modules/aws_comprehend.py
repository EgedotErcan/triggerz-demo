import boto3
import os
from dotenv import load_dotenv

class Comprehend():
    
    def __init__(self,string_data):
        load_dotenv()
        REGION_NAME = os.getenv("REGION_NAME")
        AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCES_KEY = os.getenv("AWS_SECRET_ACCES_KEY")
        self.data = [string_data]
        self.comprehend = boto3.client('comprehend', 
                        region_name=f"{REGION_NAME}",
                        aws_access_key_id=f"{AWS_ACCESS_KEY_ID}",
                        aws_secret_access_key=f"{AWS_SECRET_ACCES_KEY}")
    
    def comprehend_file(self):
        data_output = self.comprehend.batch_detect_key_phrases(TextList=self.data, LanguageCode='en')
        return data_output