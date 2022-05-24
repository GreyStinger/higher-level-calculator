from typing import Optional

import logging
import sys


# logger setup function
def setup_logger(log_level = Optional[str]) -> bool:
    """
    Creates a default logger for the package.

    :param log_level: logging level to use
    :return: True if logger was created successfully, False if not
    """
    
    try: 
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # create formatter and add to ch
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return True

    except Exception as e:
        print(e)
        return False
