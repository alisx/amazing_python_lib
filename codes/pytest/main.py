# pip install pytest

import pytest

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
    

def test_answer():
    assert inc(3) == 5  # 这将会失败，因为  3 + 1 != 5
    

@pytest.mark.parametrize("input,expected", [(1,2), (3,4), (5,6)])
def test_increment(input, expected):
    assert inc(input) == expected
    
@pytest.fixture
def input_value():
    return 39

def test_divisible_by_three(input_value):
    assert input_value % 3 == 0