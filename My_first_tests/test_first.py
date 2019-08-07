import pytest
from new_1 import New

def test_summa():
    '''Проверка функции возрата суммы двух переданных аругментов'''

    assert New.sum_num(1, 2) == 3
    assert New.sum_num("abc", "def") == "abcdef"

def test_list():

    assert New.create_list(9) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert len(New.create_list(9)) == 9
