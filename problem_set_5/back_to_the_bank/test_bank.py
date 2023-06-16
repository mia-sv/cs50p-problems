import pytest

from bank import value


def test_0():
    assert value("hello") == 0
    assert value("hello world") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_20():
    assert value("hi") == 20
    assert value("hi world") == 20
    assert value("hey") == 20
    assert value("Hi") == 20


def test_100():
    assert value("olá") == 100
    assert value("olá world") == 100
    assert value("oi") == 100


def test_numbers():
    assert value("123") == 100
    assert value("123 hello") == 100


def test_punctuation():
    assert value("!?.") == 100
    assert value("!?. hello") == 100


def test_empty():
    assert value("") == 100
