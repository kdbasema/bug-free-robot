"""
File for testing the math.py module
"""

import bug_free_robot as bfr
import pytest


def test_add():
    assert bfr.math.add(5, 2) == 7
    assert bfr.math.add(3, 8) == 11


testdata  = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99),
    (11, 0, 0),
    (0, 0, 0),
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert bfr.math.mult(a, b) == expected
    assert bfr.math.mult(b, a) == expected


def test_div():
    assert bfr.math.div(5, 5) == 1
    assert bfr.math.div(9, 3) == 3


def test_subtract():
    assert bfr.math.subtract(5, 2) == 3
    assert bfr.math.subtract(3, 8) == -5
   

def test_power():
    assert bfr.math.power(2, 3) == 8
    assert bfr.math.power(3, 3) == 27


def test_degtorad():
    assert bfr.math.degtorad(45) == 3.14159 / 4
    assert bfr.math.degtorad(180) == 3.14159


def test_radtodeg():
    assert bfr.math.radtodeg(3.14159) == 180
    assert bfr.math.radtodeg(3.14159 * 0.5) == 90
