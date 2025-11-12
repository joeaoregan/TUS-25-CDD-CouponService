import pytest

def calc_area(length, width):
    return length * width

assert calc_area(0.1, 0.2) = pytest.approx(0.02, rel=1e-4)