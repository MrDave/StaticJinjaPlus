import pytest


def func(x):
    return x + 1


def test_correct_answer():
    assert func(4) == 5


@pytest.mark.skip(reason="Example of failed autotest.")
def test_wrong_answer():
    assert func(10) == 5
