"""Logging to both file and widget"""
import logging
import os
from pathlib import Path
import sys

from uvicorn.logging import DefaultFormatter


# Instantiate LOGGER
LOGGER = logging.getLogger("aiida-optimade")
LOGGER.setLevel(logging.DEBUG)

# Save a file with all messages (DEBUG level)
ROOT_DIR = Path(__file__).parent.parent.parent.resolve()
LOGS_DIR = ROOT_DIR.joinpath("logs/")
LOGS_DIR.mkdir(exist_ok=True)

# Set handlers
FILE_HANDLER = logging.handlers.RotatingFileHandler(
    LOGS_DIR.joinpath("aiida_optimade.log"), maxBytes=1000000, backupCount=5
)
FILE_HANDLER.setLevel(logging.DEBUG)

CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
CONSOLE_HANDLER.setLevel(os.getenv("AIIDA_OPTIMADE_LOG_LEVEL", "INFO"))

# Set formatters
FILE_FORMATTER = logging.Formatter(
    "[%(levelname)-8s %(asctime)s %(filename)s:%(lineno)d] %(message)s",
    "%d-%m-%Y %H:%M:%S",
)
FILE_HANDLER.setFormatter(FILE_FORMATTER)

CONSOLE_FORMATTER = DefaultFormatter("%(levelprefix)s %(name)s - %(message)s")
CONSOLE_HANDLER.setFormatter(CONSOLE_FORMATTER)

# Finalize LOGGER
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)
