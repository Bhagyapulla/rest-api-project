import pytest
from my_functions import add,subtract,multiply,divide

def test_add_positive_numbers():
    assert add(2,3)==5
    assert add(10,0)==10
    assert add(0,0)==0

def test_add_negative_numbers():
    assert add(-1,-1)==-2
    assert add(-5,2)==-3
    assert add(0, 0) == 0
def test_subtract_positive_numbers():
    assert subtract(5,2)==3
    assert subtract(10,10)==0

def test_multiply_positive_numbers():
    assert multiply(5,2)==10
    assert multiply(10,10)==0
    assert multiply(2,3)==6


def test_divide_positive_numbers():
    assert divide(6,3)==2.0
    assert divide(10,1)==10

def test_divide_by_zero():
    with pytest.raises(ValueError,match="cannot")
