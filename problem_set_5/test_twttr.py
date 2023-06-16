import pytest

from twttr import shorten


def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("AeIoU") == ""
    assert shorten("maria") == "mr"
    assert shorten("FILIPE") == "FLP"

def test_consonants():
    assert shorten("bcdfgh") == "bcdfgh"
    assert shorten("BCDFGH") == "BCDFGH"
    assert shorten("BcDfGh") == "BcDfGh"

def test_length():
    assert len(shorten("maria")) == 2
    assert len(shorten("FILIPE")) == 3


def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("!?.") == "!?."