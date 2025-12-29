import os
import sys

sys.path.append(os.path.dirname(__file__))

from lec6_recursion_dictionaries import fib, fib_efficient


def test_fib_small_values():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8


def test_fib_efficient_matches_fib_for_n_ge_1():
    d = {1: 1, 2: 2}
    for n in range(1, 15):
        assert fib_efficient(n, d) == fib(n)

