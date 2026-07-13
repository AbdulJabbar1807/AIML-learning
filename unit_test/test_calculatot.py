import pytest

from calculator import square

def test_positive_number():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_number():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")