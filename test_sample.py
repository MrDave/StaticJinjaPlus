def func(x):
    return x + 1


def test_correct_answer():
    assert func(4) == 5


def test_wrong_answer():
    assert func(10) == 5
