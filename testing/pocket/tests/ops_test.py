from pocket.ops import addition, subtraction, division


def test_addition_zero():
    assert addition(1, 0) == 1


def test_add():
    assert addition(0, 1) == 1


def test_subtraction():
    assert subtraction(1, 4) == -3


def test_division():
    assert division(1, 4) == .25
