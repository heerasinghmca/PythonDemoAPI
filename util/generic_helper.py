import random
import string
import sys
import traceback
from datetime import datetime, timedelta

from util.log_helper import getLogger

logger = getLogger()


def generate_random_email_address(string_length, prefix_val=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=string_length))
    if not prefix_val:
        email = random_string + "@mailinator.com"
    else:
        email = prefix_val + "_" + random_string + "@mailinator.com"
    return email


def generate_random_string(string_length, prefix_val=None, suffix_val=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=string_length))
    if prefix_val:
        random_string = prefix_val + random_string
    if suffix_val:
        random_string = random_string + suffix_val
    return random_string


def get_error_trace():
    ex_type, ex_value, ex_traceback = sys.exc_info()
    trace_back = traceback.extract_tb(ex_traceback)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

    logger.exception(f'Exception type: {ex_type.__name__}  Exception message: {ex_value} Stack trace: {stack_trace}')


def get_back_date(no_of_days_from_today, date_format="%Y-%m-%d-%H:%M:%S"):
    temp_date = datetime.now() - timedelta(days=no_of_days_from_today)
    formatted_date = temp_date.strftime(date_format)
    return formatted_date
