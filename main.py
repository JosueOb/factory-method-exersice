# import PyPDF2
# #
# document = PyPDF2.PdfReader("docs/label-test.pdf").getDocumentInfo()
# print(type(document))
import pydantic

import io


# Read the pdf file and convert to bytes
class Document(pydantic.BaseModel):
    content: bytes
    title: str = "This is a PDF file"


with open("docs/label-test.pdf", 'r') as pdf:
    file = io.TextIOWrapper(pdf)
    print(type(file))
