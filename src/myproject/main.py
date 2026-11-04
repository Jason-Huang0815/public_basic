# src/myproject/main.py

import logging

from myproject.core.logic import do_something
from myproject.utils.logger import setup_logger


def main():
    setup_logger()

    logger = logging.getLogger(__name__)
    logger.info("Running...")

    try:
        do_something()
    except Exception as e:
        logger.exception("ERROR: ", e)


if __name__ == "__main__":
    main()
