import CanadianTax
def test_taxForLow():
     assert CanadianTax.taxForLow(15000) == 2250.0
def test_taxForMedium():
    print(CanadianTax.taxForMedium(25000))
    assert CanadianTax.taxForMedium(25000) == 2505.85
def test_taxForMediumU():
    print(CanadianTax.taxForMedium(60000))
    assert CanadianTax.taxForMedium(60000) == 9680.85
def test_taxForMediumUpper():
    assert CanadianTax.taxForMedium(90000) == 15830.85
def test_taxForHighIncome():
    assert CanadianTax.taxForHighIncome(100000) == 12296.57
def test_computing():
    assert CanadianTax.computing(15000) ==2250.0
