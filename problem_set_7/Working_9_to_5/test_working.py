import pytest

from working import convert


def test_valid_convert():
    assert convert("2 AM to 3 AM") == ("02:00 to 03:00")
    assert convert("9:00 AM to 5:00 PM") == ("09:00 to 17:00")
    assert convert("5 PM to 9 AM") == ("17:00 to 09:00")
    assert convert("12 AM to 3:00 PM") == ("00:00 to 15:00")
    assert convert("12:12 PM to 2:20 AM") == ("12:12 to 02:20")


def test_invalid_convert():
    with pytest.raises(ValueError):
        convert("2 AM 3 AM")
    with pytest.raises(ValueError):
        convert("2 AM to  3 AM")
    with pytest.raises(ValueError):
        convert("6 AM to 23 AM")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("1 to 2")
    with pytest.raises(ValueError):
        convert("15 AM to 12 PM")
    with pytest.raises(ValueError):
        convert("10:60 AM to 12:78 PM")
