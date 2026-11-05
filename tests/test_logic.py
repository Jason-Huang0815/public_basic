# tests/test_logic.py

import pytest

from myproject.core.logic import calculate_discount, get_user_full_name


def test_calculate_discount_positive():
    """A 20% discount on 100$ should be 80$"""

    assert calculate_discount(100, 0.2) == 80


def test_calculate_discount_negative():
    """Get an error when discount rate is beyond 1"""

    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


def test_get_user_full_name(user_sample):
    # the param name should be same as the one in fixture
    """Pytest will run the corresponding fixture function"""

    assert get_user_full_name(user_sample) == "John Doe"
