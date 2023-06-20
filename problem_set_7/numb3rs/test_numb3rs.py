import pytest

from numb3rs import validate


def test_dots():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.1.") == False


def test_digits():
    assert validate("256.256.256.256") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("0.1.2.3") == True
    assert validate(".1.1.1") == False
    assert validate("1111") == False
    assert validate("1234.1.1.1") == False
    assert validate("255.0.0.0") == True
    assert validate("256.1.2.3") == False
    assert validate("1.256.2.3") == False
    assert validate("1.2.256.3") == False
    assert validate("1.2.3.256") == False
