import pytest

from plates import is_valid


def test_allnumbers():
    assert is_valid("154865") == False
    assert is_valid("154MAS") == False


def test_allletters():
    assert is_valid("ABC") == True
    assert is_valid("ABCDEF") == True


def test_len():
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("") == False


def test_digit():
    assert is_valid("12345") == False
    assert is_valid("1ABC") == False
    assert is_valid("12ABC") == False
    assert is_valid("AB123") == True
    assert is_valid("12AB3") == False
    assert is_valid("AB25AB") == False


def test_zero():
    assert is_valid("AB00") == False
    assert is_valid("ABC012") == False
    assert is_valid("ABC120") == True


def test_punctuation():
    assert is_valid("AB!?.") == False
    assert is_valid("AB C 1") == False
    assert is_valid("AB,C,1") == False
