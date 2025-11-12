import pytest

from calc_mean_v7 import calc_mean

def test_calc_mean_raises_value_error_on_empty_list():
    with pytest.raises(ValueError) as e:
        calc_mean([]) # emtpy list
    assert str(e.value) == "Cannot calculate the mean of an empty list"

def test_calc_mean_non_numeric_raises_type_error():
    with pytest.raises(TypeError) as e:
        calc_mean([1, 'a', 3])
    assert str(e.value) == "All elements in the list must be numeric."

if __name__ == "__main__":
    pytest.main([__file__, "-v"])