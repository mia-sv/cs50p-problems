from seasons import date_to_minutes
import pytest


def test_valid():
    assert (
        date_to_minutes("2005-02-26")
        == "Nine million, six hundred forty-eight thousand"
    )
    assert (
        date_to_minutes("1975-05-17")
        == "Twenty-five million, three hundred twelve thousand, three hundred twenty"
    )
    assert (
        date_to_minutes("1999-12-30")
        == "Twelve million, three hundred sixty-two thousand, four hundred"
    )


def test_invalid():
    with pytest.raises(ValueError):
        date_to_minutes("3")
    with pytest.raises(ValueError):
        date_to_minutes("March 1st")
    with pytest.raises(ValueError):
        date_to_minutes("2005/02/26")
    with pytest.raises(ValueError):
        date_to_minutes("26-02-2005")
