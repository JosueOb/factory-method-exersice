from __future__ import annotations
from abc import ABC, abstractmethod

import pydantic


class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, value: str):
        pass


# Services
class InvoiceFactory(DocumentFactory):
    def create_document(self, value: str) -> Document:
        # Here, we need to change
        text = f"This is a single string ==> {value}"
        return Document(content=text)


class ShippingLabelFactory(DocumentFactory):
    def create_document(self, value: str) -> Document:
        # We need to create a zpl code
        text = f'This is a binary data ==> {value}'
        return Document(content=text)


# Object domain
class Document(pydantic.BaseModel):
    content: str | bytes


# class InvoiceDocument(Document):
#     def __init__(self, content):
#
#     def get(self) -> str:
#         return "Invoice created.."
#
#
# class ShippingLabelDocument(Document):
#     def get(self) -> str:
#         return "Shipping label created"


if __name__ == "__main__":
    """Service"""
    invoice = InvoiceFactory()
    shipping_label = ShippingLabelFactory()
    print(f'This is a Invoice ==> {invoice.create_document("INVOICE TEST")}')
    print(f'This is a Shipping Label ==> {shipping_label.create_document("SHIPPING LABEL TEST")}')
