# test_calculator.py
from calculator import add  # calculator.py 파일의 add 함수를 가져옴

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2
