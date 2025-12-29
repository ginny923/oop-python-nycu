import os
import sys

sys.path.append(os.path.dirname(__file__))

from lec6_recursion_dictionaries import (
    is_palindrome,
    lyrics_to_frequencies,
    most_common_words,
    words_often,
)


def test_is_palindrome_examples():
    assert is_palindrome("eve") is True
    assert is_palindrome("Able was I, ere I saw Elba") is True
    assert is_palindrome("Is this a palindrome") is False


def test_lyrics_to_frequencies_basic():
    lyrics = ["a", "b", "a", "c", "a", "b"]
    freqs = lyrics_to_frequencies(lyrics)
    assert freqs["a"] == 3
    assert freqs["b"] == 2
    assert freqs["c"] == 1


def test_most_common_words_basic():
    freqs = {"a": 3, "b": 2, "c": 1}
    words, best = most_common_words(freqs)
    assert best == 3
    assert "a" in words


def test_words_often_min_times_2():
    # x:3, y:4, z:1
    freqs = {"x": 3, "y": 4, "z": 1}
    result = words_often(freqs, 2)

    # 先挑 y:4，再挑 x:3；z 不達門檻
    assert result[0][1] == 4 and "y" in result[0][0]
    assert result[1][1] == 3 and "x" in result[1][0]
