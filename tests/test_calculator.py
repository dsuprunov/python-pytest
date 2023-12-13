import pytest
from contextlib import nullcontext as does_not_raise
from src.calculator import Calculator


class __SkipTestCalculator:

    @pytest.mark.parametrize('a, b, c, exp', [
        (3, 2, 1.5, does_not_raise()),
        (0, 2, 0, does_not_raise()),
        (3, '2', 1.5, pytest.raises(TypeError)),
        (1, 0, 0, pytest.raises(ZeroDivisionError))
    ])
    def test_div(self, a, b, c, exp):
        with exp:
            assert Calculator().div(a, b) == c

    @pytest.mark.parametrize('a, b, c, exp', [
        (1, 2, 3, does_not_raise()),
        (5, -1, 4, does_not_raise()),
        ('5', -1, 4, pytest.raises(TypeError)),
    ])
    def test_add(self, a, b, c, exp):
        with exp:
            assert Calculator().add(a, b) == c
