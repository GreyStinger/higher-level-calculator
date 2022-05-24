from logging import Formatter, StreamHandler, FileHandler
from logging.handlers import TimedRotatingFileHandler
from typing import Optional

import logging
import sys

def get_file_handler(formatter: Formatter, log_file: Optional[str] = None) -> FileHandler:
    """
    Returns a file handler for the package.

    :param (Formatter) formatter: Formatter to use
    :param (str) log_file: logfile to use, relative to package root
        Use None for only console output.
    :return (logging.FileHandler) File handler for the package
    """

    try:
        if log_file is None:
            return None
        else:
            fh = TimedRotatingFileHandler(log_file, when='midnight')
            fh.setFormatter(formatter)
            return fh
            
    except Exception as e:
        print(e)
        return None

def get_console_handler(formatter: Formatter) -> StreamHandler:
    """
    Returns a console handler for the package.

    :param (Formatter) formatter: Formatter to use
    :return (logging.FileHandler) File handler for the package
    """

    try:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        return ch
    except Exception as e:
        print(e)
        return None


# logger setup function
def setup_logger(logfile: str = Optional[str], log_level: str = Optional[str]) -> bool:
    """
    Creates a default logger for the package.

    :param (str) log_level: logging level to use
        Use DEBUG for development, INFO or None for production.
    :param (str) logfile: logfile to use, relative to package root
        Use None for console output.

    :return (bool) True if logger was created successfully, False if not
    """
    
    try: 
        logger = logging.getLogger('logger')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_level is None or log_level == "INFO":
            logger.setLevel(logging.INFO)
        elif log_level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        else:
            print("Invalid log level: " + log_level)
            return False

        if logfile is not None:
            file_handler = get_file_handler(formatter, logfile)
            logger.addHandler(file_handler)
        console_handler = get_console_handler(formatter)
        logger.addHandler(console_handler)

        return True

    except Exception as e:
        print(e)
        return False
