import requests
import json
import base64


def encode(data: bytes):
    """
    Return base-64 encoded value of binary data.
    """
    return base64.b64encode(data)


def decode(data: str):
    """
    Return decoded value of a base-64 encoded string.
    """
    return base64.b64decode(data.encode())


def get_pdf_data(filename):
    """
    Open pdf file in binary mode,
    return a string encoded in base-64.
    """
    with open(filename, 'rb') as file:
        return encode(file.read())


def send_pdf_data(filename_list, encoded_pdf_data):
    data = {}
    # *Put whatever you want in data dict*
    # Create content dict.
    content = [dict([("name", filename), ("data", pdf_data)])
               for (filename, data) in zip(filename_list, encoded_pdf_data)]
    data["content"] = content

    data = json.dumps(data) # Convert it to json.
    requests.post("http://yourserveradders", data=data)


def main():
    filename_list = ["pdf_name_1.pdf", "pdf_name_2.pdf"]
    pdf_blob_data = [get_pdf_data(filename) for filename
                     in filename_list]

if __name__ == '__main__':
    main()