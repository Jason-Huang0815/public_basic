# src/myproject/utils/logger.py

import logging
import sys


def setup_logger(level=logging.INFO):
    """Configure global logger, uniform the format"""

    # 1. define the logging format (time - level - module: line - message)
    log_format = "%(asctime)s - [%(levelname)s] - %(name)s: %(lineno)s - %(message)s"

    # output the log into consoler
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("app.log", encoding="utf-8"),
        ],
        force=True,
    )
