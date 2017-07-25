"""
File for testing the math.py module
"""

import bug_free_robot
import pytest


def test_add():
    assert bug_free_robot.add(5, 2) == 7
    assert bug_free_robot.add(3, 8) == 11


def test_mult():
    assert bug_free_robot.mult(5, 2) == 10
    assert bug_free_robot.mult(3, 8) == 24


def test_div():
    assert bug_free_robot.div(5, 5) == 1
    assert bug_free_robot.div(9, 3) == 3



def test_mult():
    assert bug_free_robot.subtract(5, 2) == 3
    assert bug_free_robot.subtract(3, 8) == -5



def test_degtorad():
    assert bug_free_robot.degtorad(45) == 3.14159 / 4
    assert bug_free_robot.degtorad(180) == 3.14159


def test_radtodeg():
    assert bug_free_robot.radtodeg(3.14159) == 180
    assert bug_free_robot.radtodeg(3.14159 * 0.5) == 90

