"""
File for testing the math.py module
"""

import bug_free_robot
import pytest


def test_add():
    assert bug_free_robot.add(5, 2) == 7
    assert bug_free_robot.add(3, 8) == 11
