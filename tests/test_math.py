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
