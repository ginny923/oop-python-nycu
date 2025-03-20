import add_path
import pytest
import mit_ocw_exercises.lec6_recursion_dictionaries as lec6

def test_fibonacci():
    assert lec6.fibonacci(0) == 0
    assert lec6.fibonacci(1) == 1
    assert lec6.fibonacci(2) == 1
    assert lec6.fibonacci(3) == 2
    assert lec6.fibonacci(4) == 3
    assert lec6.fibonacci(5) == 5
    assert lec6.fibonacci(6) == 8
    assert lec6.fibonacci(7) == 13
    assert lec6.fibonacci(8) == 21
    assert lec6.fibonacci(9) == 34
    assert lec6.fibonacci(10) == 55
    assert lec6.fibonacci(11) == 89
    assert lec6.fibonacci(12) == 144
    assert lec6.fibonacci(13) == 233
    assert lec6.fibonacci(14) == 377
    assert lec6.fibonacci(15) == 61


def tower ():
    assert lec6.tower(1, 'P1', 'P2', 'P3') == None
    assert lec6.tower(2, 'P1', 'P2', 'P3') == None
    assert lec6.tower(3, 'P1', 'P2', 'P3') == None
    assert lec6.tower(4, 'P1', 'P2', 'P3') == None
    assert lec6.tower(5, 'P1', 'P2', 'P3') == None
    assert lec6.tower(6, 'P1', 'P2', 'P3') == None
