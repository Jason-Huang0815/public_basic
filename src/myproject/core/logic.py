# src/myproject/core/logic.py

import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)


def do_something():
    logger.info("I am doing something")


def calculate_discount(price: float | int, discount_rate: float | int):
    """Calculate discount rate based on price and discount rate"""

    if not (0 <= discount_rate <= 1):
        raise ValueError("discount rate must be between 0 and 1")
    return round(price * (1 - discount_rate), 2)


def get_user_full_name(user: dict) -> str:
    """Return full name of user"""

    return f"{user['first_name']} {user['last_name']}"


def get_db_url() -> str:
    """Decide which database to link according to environment"""

    env = os.environ.get("APP_ENV", "dev")

    if env == "prod":
        return "postgresql://prod-db:5432"
    return "sqlite:///local.db"


def is_vip_active(expire_date_str: str) -> bool:
    """Judge whether vip is active or not, format: YYYY-MM-DD"""

    expire_date = datetime.strptime(expire_date_str, "%Y-%m-%d")
    now = datetime.now()
    return now <= expire_date
