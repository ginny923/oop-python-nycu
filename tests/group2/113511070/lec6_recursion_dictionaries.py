# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016
@author: WELG

Lecture code (整理成可被 pytest 匯入測試的版本)

包含：
- Towers of Hanoi
- Fibonacci (naive + memoization)
- Palindrome
- Lyrics word frequencies + most common + words often
"""

from __future__ import annotations
from typing import Dict, List, Tuple, Any


# =========================
# Towers of Hanoi
# =========================
def printMove(fr: Any, to: Any) -> None:
    print("move from " + str(fr) + " to " + str(to))


def Towers(n: int, fr: Any, to: Any, spare: Any) -> None:
    """
    Prints the moves to solve Towers of Hanoi.
    """
    if n <= 0:
        raise ValueError("n must be >= 1")
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)


# =========================
# Fibonacci
# =========================
def fib(x: int) -> int:
    """
    assumes x an int >= 0
    returns Fibonacci of x with base:
      fib(0)=1, fib(1)=1
    """
    if x < 0:
        raise ValueError("x must be >= 0")
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)


def fib_efficient(n: int, d: Dict[int, int]) -> int:
    """
    Memoized Fibonacci that matches fib() definition:
      fib(0)=1, fib(1)=1
    Usage:
      d = {0: 1, 1: 1}
      fib_efficient(34, d)
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in d:
        return d[n]
    ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
    d[n] = ans
    return ans


# =========================
# Palindrome
# =========================
def is_palindrome(s: str) -> bool:
    def to_chars(ss: str) -> str:
        ss = ss.lower()
        ans = ""
        for c in ss:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def is_pal(ss: str) -> bool:
        if len(ss) <= 1:
            return True
        return ss[0] == ss[-1] and is_pal(ss[1:-1])

    return is_pal(to_chars(s))


# =========================
# Dictionaries: lyrics frequencies
# =========================
def lyrics_to_frequencies(lyrics: List[str]) -> Dict[str, int]:
    myDict: Dict[str, int] = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def most_common_words(freqs: Dict[str, int]) -> Tuple[List[str], int]:
    """
    Return (words, bestCount).
    If multiple words tie for max frequency, returns all of them.
    """
    if not freqs:
        raise ValueError("freqs must not be empty")
    best = max(freqs.values())
    words: List[str] = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs: Dict[str, int], minTimes: int) -> List[Tuple[List[str], int]]:
    """
    Repeatedly take the most common words; if their count >= minTimes, record them
    and delete them from the dict, then continue. Stops when max count < minTimes.

    Note: This function MUTATES freqs (deletes keys).
    """
    if minTimes <= 0:
        raise ValueError("minTimes must be >= 1")

    result: List[Tuple[List[str], int]] = []
    while freqs:
        words, best = most_common_words(freqs)
        if best < minTimes:
            break
        result.append((words, best))
        for w in words:
            del freqs[w]
    return result
