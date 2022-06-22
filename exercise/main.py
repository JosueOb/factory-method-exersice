from __future__ import annotations
from abc import ABC, abstractmethod

class Document_Creator(ABC):
    @abstractmethod
    def create_document(self):
        pass

    def some_operation(self) -> str:
        document = self.create_document()
        result = f"Creator: The same creator's code has just worked with {document.operation()}"
        return result

class InvoiceCreator(Document_Creator):
    def create_document(self) -> Document:
        return InvoiceDocument()

class ShippingLabelCreator(Document_Creator):
    def create_document(self) -> Document:
        return ShippingLabelDocument()

class Document(ABC):
    @abstractmethod
    def get(self) -> str:
        pass

class InvoiceDocument(Document):
    def get(self) -> str:
        return "Invoice creado."

class ShippingLabelDocument(Document):
    def get(self) -> str:
        return "Shipping label creado"

def document_logic(document_creator: Document_Creator) -> None:
    var = document_creator.create_document()
    print(var)

if __name__ == "__main__":
 document_logic(InvoiceCreator())
