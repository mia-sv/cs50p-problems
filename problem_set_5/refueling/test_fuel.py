import pytest

from fuel import convert

from fuel import gauge


def test_input():
    with pytest.raises(ValueError):
        convert("1.1")
    with pytest.raises(ValueError):
        convert("1.1/1.2")
    with pytest.raises(ValueError):
        convert("2/1")


def test_convert():
    assert convert("1/3") == 33
    assert convert("1/1") == 100
    assert convert("1/1000") == 0


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(99.5) == "F"
    assert gauge(60) == "60%"
