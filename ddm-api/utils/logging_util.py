import logging
import os

def logger_config(log_level=logging.INFO, log_file="app.log"):
    """
    Configure the logger with the desired log level and file name.
    
    Args:
        log_level (int): Log level for the logger (e.g., logging.INFO, logging.DEBUG).
        log_file (str): File name for log files.

    Returns:
        logger (logging.Logger): Logger instance.
    """
    # Create the log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a formatting object for the logger
    log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s")

    # Configure the logger
    logger = logging.getLogger("app_logger")
    logger.setLevel(log_level)

    # Create a file handler to store log messages in a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_formatter)

    # Create a stream handler to send log messages to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(log_formatter)

    # Add the file handler and stream handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
