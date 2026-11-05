# tests/test_logic.py

import pytest
from freezegun import freeze_time

from myproject.core.logic import (
    calculate_discount,
    get_db_url,
    get_user_full_name,
    is_vip_active,
)


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


def test_get_db_url(monkeypatch):
    # 1. for default, should be dev local db
    assert get_db_url() == "sqlite:///local.db"

    # 2. disguise as production env with monkeypatch
    monkeypatch.setenv("APP_ENV", "prod")
    assert get_db_url() == "postgresql://prod-db:5432"


@freeze_time("2021-06-01")
def test_is_vip_active(monkeypatch):
    expire_date = "2023-12-31"

    assert is_vip_active(expire_date) is True
