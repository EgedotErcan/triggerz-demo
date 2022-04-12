import boto3

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