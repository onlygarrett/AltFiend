import logging
import sys
from logging.handlers import TimedRotatingFileHandler

DATEFMT = "%d/%b/%Y %H:%M:%S"
FORMATTER = logging.Formatter(
    datefmt=DATEFMT,
    fmt="[%(asctime)s] : %(levelname)s : \
    [%(name)s.%(funcName)s:%(lineno)d]  : %(message)s",
)
LOG_FILE = "src/error_handling/logs/error.log"


def stream_logger():
    """
    This function creates and returns a stream handler for logging.

    The stream handler is a StreamHandler that writes log messages to the standard output (sys.stdout).
    It uses the global FORMATTER to format log messages.

    Parameters:
    None

    Returns:
    stream_handler (logging.StreamHandler): A configured stream handler for logging.
    """
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(FORMATTER)
    return stream_handler


def log_file_handler():
    """
    This function creates and returns a TimedRotatingFileHandler for logging.

    The TimedRotatingFileHandler is a handler that rotates the log file at specific intervals.
    It uses the global FORMATTER to format log messages and writes them to the LOG_FILE.

    Parameters:
    None

    Returns:
    file_handler (TimedRotatingFileHandler): A configured TimedRotatingFileHandler for logging.
    """
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def base_logger(logger_name) -> logging.Logger:
    """
    This function creates and configures a logger with two handlers: a StreamHandler for logging to the standard output
    and a TimedRotatingFileHandler for logging to a file. The logger is set to the ERROR level and propagation is disabled.

    Parameters:
    logger_name (str): The name of the logger.

    Returns:
    logger (logging.Logger): A configured logger with the specified name and handlers.
    """
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.ERROR)
    logger.addHandler(stream_logger())
    logger.addHandler(log_file_handler())

    logger.propagate = False
    return logger
