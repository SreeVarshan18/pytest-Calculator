import calculator

def test_add2no():
    x = 10
    y = 20
    res = calculator.add2no(x, y)
    assert res == x+y

def test_sub2no():
    x = 40
    y = 20
    res = calculator.sub2no(x, y)
    assert res == x - y

def test_nul2no():
    x = 2
    y = 5
    res = calculator.mul2no(x, y)
    assert res == x*y

def test_div2no():
    x = 5
    y = 2
    res = calculator.div2no(x, y)
    assert res == x/y

