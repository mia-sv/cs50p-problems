import pytest

from um import count


def test_valid():
    assert count("um, hello") == 1
    assert count("hello, um") == 1
    assert count("um, hello, um") == 2
    assert count("hello, um, hello") == 1
    assert count("um um um") == 3
    assert count("hello um") == 1
    assert count("umi um um") == 2
    assert count("hello, um hello, um hello, um hello, um hello, um") == 5
    assert count("um") == 1
    assert count(" um") == 1
    assert count("um um um um um um um um um um um um") == 12
    assert count("um um um    um um    um um   um    um um um um") == 12
    assert count("This is, um... CS50.") == 1
    assert count("Um...ok") == 1


def test_invalid():
    assert count("yum, hello") == 0
    assert count("tulum, mexico") == 0
    assert count("mu mu mu mu") == 0
    assert count("hello tum") == 0
