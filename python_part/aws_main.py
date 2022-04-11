from aws_transcribe import Transcribe
from aws_comprehend import Comprehend
from aws_assign_pdf import Assign

class Core():
    def __init__(self,file_name,job_name):
        self.file_name = file_name
        self.job_name = job_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.job_name)
        self.assign_object = Assign(self.file_name,Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        self.assign_object.assign_pdf()
            
        


