import pytest
from lec6_recursion_dictionaries import (
    is_palindrome,
    lyrics_to_frequencies,
    most_common_words,
    words_often,
)


def test_is_palindrome_basic():
    assert is_palindrome("eve") is True
    assert is_palindrome("Is this a palindrome") is False


def test_is_palindrome_ignores_case_and_non_letters():
    assert is_palindrome("Able was I, ere I saw Elba") is True


def test_lyrics_to_frequencies_and_most_common():
    lyrics = ["a", "b", "a", "c", "a", "b"]
    freqs = lyrics_to_frequencies(lyrics)
    assert freqs == {"a": 3, "b": 2, "c": 1}

    words, best = most_common_words(freqs)
    assert best == 3
    assert words == ["a"]


def test_words_often_groups_and_mutates_dict():
    lyrics = ["x", "y", "x", "z", "y", "x", "y", "y"]
    freqs = lyrics_to_frequencies(lyrics)  # x:3, y:4, z:1

    result = words_often(freqs, 2)

    assert result == [(["y"], 4), (["x"], 3)]
    assert freqs == {"z": 1}


def test_most_common_words_rejects_empty():
    with pytest.raises(ValueError):
        most_common_words({})
