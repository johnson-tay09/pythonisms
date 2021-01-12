import pytest
from pythonisms import Pythonisms


def test_write_text():
    text = "send it through"
    actual = Pythonisms.return_text(text)
    expected = "send it through"
    assert actual == expected


def test_add_energy():
    text = "debugging"
    actual = Pythonisms.add_emphasis(text)
    expected = "I LOVE debugging MORE THAN ANYTHING IN THE WORLD!"
    assert actual == expected


def test_decorator():
    text = "you can call me Lazer."
    actual = Pythonisms.taylor_quote(text)
    expected = '"you can call me Lazer." - Taylor'
    assert actual == expected


def test_fill_spaces():
    text = "test for space"
    actual = Pythonisms.fill_spaces(text)
    expected = ["testXforXspace"]
    assert actual == expected
