import pytest
from euro_to_gbp_solutions import convert_euro_to_gbp

def test_convert_euro_to_gbp_fails():
    # This might fail with AssertionError due to floating point rounding
    assert convert_euro_to_gbp(0.1, 0.87) == 0.087

def test_convert_euro_to_gbp_passes():
    # pytest.approx allows for tying rounding differences
    assert convert_euro_to_gbp(0.1, 0.87) == pytest.approx(0.087)

if __name__=="__main__":
    # pytest.main([__file__])
    pytest.main([__file__,"-v"])