from newby import *
import pytest

def test_s(first):
    '''
        Проверка функции возрата суммы двух переданных аругментов
    '''
    assert calculate(1, 2) == 3, "Должно быть 3"
    assert calculate("abc", "def") == "abcdef"


def test_l(first):
    '''
        Проверка значений создаваемого списка
    '''
    assert create_tuple(9) == (0, 1, 2, 3, 4, 5, 6, 7, 8)
    assert len(create_tuple(9)) == 9

def test_fac():
    '''
        Функция вычисляющая факториал
    '''
    assert factorial(5) == 120


def test_five(fixture_with_params):
    '''
        Проверка функции вычисляющей факторил числа, с переданным параметром из фикстуры
    '''
    assert factorial(fixture_with_params) == 3628800


def test_binomial(first):
    '''
        Функция вычисляющая биномиальный коэфициент
    '''
    assert binomial(10, 2) == 45
    assert binomial(2, 10) == 0
    assert binomial(0, 0) == 1

def test_the_fix(third_fixture):
    '''
        Проверка функции - фискстуры, возращающая сумму четных чисел из списка до 20
    '''
    assert third_fixture == 90


@pytest.mark.parametrize("test_input", ["1", "2", "3", "4"])
    #параметризация теста, проверяющего что возвращаемый тип строка
class TestClassPar:

    def test_four(self, test_input):
        s = test_input + " box"
        assert isinstance(s, str)
