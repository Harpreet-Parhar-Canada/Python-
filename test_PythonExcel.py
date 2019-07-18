import python_excel


def test_Sheets():
        assert  PythonExcel.x.workSheets() == ['Clients', 'Invoices', 'Items Sold', 'Product Inventory']


