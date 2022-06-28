from temp.exercise.main import InvoiceFactory, ShippingLabelFactory, Document


def test_invoice_factory():
    
    assert InvoiceFactory().create_document('INVOICE TEST') == Document(content='This is a single string ==> INVOICE TEST')

def test_shipping_label_factory():
    assert ShippingLabelFactory().create_document('SHIPPING LABEL TEST') == Document(content='This is a binary data ==> SHIPPING LABEL TEST')

def test_document():
    assert Document(content='This is a single string ==> INVOICE TEST') == Document(content='This is a single string ==> INVOICE TEST')
    assert Document(content='This is a binary data ==> SHIPPING LABEL TEST') == Document(content='This is a binary data ==> SHIPPING LABEL TEST')