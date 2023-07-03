from jar import Jar

import pytest


def test_creation():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

    with pytest.raises(ValueError):
        jar2 = Jar(-2)

    jar3 = Jar(3)
    assert jar3.capacity == 3
    assert jar3.size == 0


def test_deposit():
    jar1 = Jar(15)
    assert jar1.size == 0

    jar1.deposit(2)
    assert jar1.size == 2

    jar1.deposit(4)
    assert jar1.size == 6

    with pytest.raises(ValueError):
        jar1.deposit(10)


def test_withdraw():
    jar1 = Jar(15)
    jar1.deposit(15)
    assert jar1.size == 15

    jar1.withdraw(4)
    assert jar1.size == 11

    jar1.withdraw(5)
    assert jar1.size == 6

    with pytest.raises(ValueError):
        jar1.withdraw(10)


def test_str():
    jar1 = Jar(15)
    assert str(jar1) == ""

    jar1.deposit(2)
    assert str(jar1) == "🍪🍪"

    jar1.deposit(4)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪"

    jar1.withdraw(6)
    assert str(jar1) == ""
