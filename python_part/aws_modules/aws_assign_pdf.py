from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas as pd
import textwrap

class Assign():
    def __init__(self,file_name,keywords):
        self.file_name = file_name
        self.keywords = keywords
        self.target_file = "./2022_CG_Triggered_SF.pdf"
        self.original_file = "./2022_CG_Triggered_SF.pdf"  
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
        outputStream = open(self.original_file, "ab")
        output.write(outputStream)
        outputStream.close()
        return self.keywords

    def data_preprocessing(self):
        string_keywords_array = pd.DataFrame(self.keywords)["Text"].to_numpy(dtype="str")
        string_keywords_str = ",".join(string_keywords_array)
        self.keywords = string_keywords_str





