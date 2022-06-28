import base64


def _encode(data: bytes) -> bytes:
    """
    Return base-64 encoded value of binary data
    :param data:
    :return:
    """
    return base64.b64encode(data)


def get_pdf_data(file_name: str) -> bytes:
    """
    Open a pdf file in binary mode
    :param file_name:
    :return:
    """
    with open(file_name, 'rb') as file:
        return _encode(file.read())


print(get_pdf_data('docs/label.pdf').decode("utf-8"))
