import pytest
from lec6_recursion_dictionaries import fib, fib_efficient


def test_fib_base_cases():
    assert fib(0) == 1
    assert fib(1) == 1


def test_fib_small_values():
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8


def test_fib_efficient_matches_fib():
    d = {0: 1, 1: 1}
    for n in range(0, 15):
        assert fib_efficient(n, d) == fib(n)


def test_fib_rejects_negative():
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(ValueError):
        fib_efficient(-3, {0: 1, 1: 1})
