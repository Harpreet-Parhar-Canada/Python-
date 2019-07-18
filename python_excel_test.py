import python_excel, datetime

# Testing the Clients Class:
def test_Clients():
    a = python_excel.Clients('List')
    assert a.name == 'List'

# Teting the Product Class:
def test_Product():
    b = python_excel.Product('TV', 599.99, 5)
    assert b.name == 'TV'
    assert b.price == 599.99
    assert b.inventory == 5

# Testing the Invoice Class:
def test_Invoice():
    c = python_excel.Invoice('0001', 'May 25, 2019')
    assert c.clientid == '0001'
    assert c.date == 'May 25, 2019'
    assert c.product == ''

# Testing Helper Class:
def test_init():
    newfile = python_excel.Helper('Invoice-Example.xlsx')
    assert newfile.wb.sheetnames == ['Clients', 'Invoices', 'Items Sold', 'Product Inventory']

    # Testing make_cust_dict method:
    newfile.make_cust_dict()
    assert newfile.client_dict['0005'].name == 'Aneesha Diaz'
    assert newfile.client_dict['0016'].name == 'Ian Mellon'

    # Testing make_proct_dict method:
    newfile.make_prod_dict()
    assert newfile.prod_dict['0003'].name == 'Sound Bar'
    assert newfile.prod_dict['0003'].price == 179.99
    assert newfile.prod_dict['0003'].inventory == 253

    # Testing item method:
    newfile.item('00001')
    assert newfile.item_dict == {'0001': 1}
    newfile.item('00055')
    assert newfile.item_dict == {'0001':2, '0003':1}

    # Testing make_inv_dict method:
    newfile.make_inv_dict()
    assert newfile.inv_dict['00001'].product == {'0001':1}
    assert newfile.inv_dict['00001'].clientid == '0001'
    assert newfile.inv_dict['00001'].date == datetime.datetime(2019, 3, 16, 0, 0)






