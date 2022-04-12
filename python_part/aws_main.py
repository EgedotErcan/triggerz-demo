from aws_modules.aws_assign_pdf import Assign
from aws_modules.aws_comprehend import Comprehend
from aws_modules.aws_transcribe import Transcribe

class Core():
    def __init__(self,file_name):
        self.file_name = file_name
        self.transcribe_object = Transcribe(file_url=self.file_name,job_name=self.file_name)
        self.assign_object = Assign(self.file_name,Comprehend(self.transcribe_object.transcribe_file()).comprehend_file()['ResultList'][0]['KeyPhrases'])
        self.string_keywords = self.assign_object.assign_pdf()
            
        


