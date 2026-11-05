# tests/conftest.py

import pytest


@pytest.fixture
def user_sample():
    """This is a test data preparor, call me if you gonna test user logic"""

    return {"first_name": "John", "last_name": "Doe", "age": 28}
