# import PyPDF2
# #
# document = PyPDF2.PdfReader("docs/label-test.pdf").getDocumentInfo()
# print(type(document))
import base64
from typing_extensions import dataclass_transform
import pydantic


# Read the pdf file and convert to bytes
class Document(pydantic.BaseModel):
    content: bytes
    title: str = "This is a PDF file"


class Operation:
    def convert_to_bytes(self, label_route: str) -> bytes:
        with open(label_route, 'rb') as file:
            encode_pdf = base64.b64encode(file.read())

        return encode_pdf

    def convert_to_pdf(self, bytes_data: bytes) -> None:
        pdf_data = bytes_data.decode('utf-8')
        print(type(pdf_data))


if __name__ == "__main__":
    label_route = "./docs/label.pdf"
    operation = Operation()
    bytes_data = operation.convert_to_bytes(label_route)
    print(type(bytes_data))
    operation.convert_to_pdf(bytes_data)
