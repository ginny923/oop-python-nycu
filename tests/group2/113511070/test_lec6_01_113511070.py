import os
import sys

# 確保可 import 同資料夾的 lec6_recursion_dictionaries.py
sys.path.append(os.path.dirname(__file__))

from lec6_recursion_dictionaries import Towers


def test_hanoi_n1_prints_one_move(capsys):
    Towers(1, "P1", "P2", "P3")
    out = capsys.readouterr().out.strip().splitlines()
    assert out == ["move from P1 to P2"]


def test_hanoi_n2_prints_three_moves(capsys):
    Towers(2, "P1", "P2", "P3")
    out = capsys.readouterr().out.strip().splitlines()
    assert out == [
        "move from P1 to P3",
        "move from P1 to P2",
        "move from P3 to P2",
    ]
