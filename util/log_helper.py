import inspect
import logging
import os
from datetime import datetime


def getLogger():
    test_name = inspect.stack()[1][3]
    temp_date = datetime.now()
    current_time_value = temp_date.strftime("%Y_%m_%d-%H_%M_%S")
    cur_file_dir = os.path.dirname(os.path.realpath(__file__))
    logger = logging.getLogger(test_name)
    logger.propagate = False
    logFileName = os.path.join(cur_file_dir, '..', 'logs', current_time_value + '_' + test_name + '.log')
    file_handler = logging.FileHandler(logFileName)
    formatter = logging.Formatter(
        "%(asctime)s	%(levelname)s	%(filename)s	%(name)s	%(lineno)d	%(message)s",
        "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # sets the level for debugging
    logger.setLevel(logging.DEBUG)
    return logger
