import calculator

import pytest


@pytest.mark.parametrize("a, b, c", [(2, 3, 5), (12, 10, 22)])
def test_add2no(a, b, c):
    res = calculator.add2no(a, b)
    assert res == c


@pytest.mark.filterwarnings
def test_sub2no():
    a = 5
    b = 2
    res = calculator.sub2no(a, b)
    assert res == a - b


@pytest.mark.parametrize("a, b, c", [(3, 2, 6), (9, 4, 36)])
def test_mul2no(a, b, c):
    res = calculator.mul2no(a, b)
    assert res == c


@pytest.mark.filterwarnings
def test_div2no():
    x = 5
    y = 2
    res = calculator.div2no(x, y)
    assert res == x/y

