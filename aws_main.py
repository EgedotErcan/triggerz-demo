from aws_transcribe import Transcribe
from aws_comprehend import Comprehend
import pandas as pd

class Core():
    def __init__(self,file_name,job_name):
        self.file_name = file_name
        self.job_name = job_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.job_name)
        self.df = pd.DataFrame(Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        print(self.df.to_string())
        


