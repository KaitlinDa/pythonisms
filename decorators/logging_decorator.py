from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG)

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"'{func.__name__}' returned {result}")
        return result
    return wrapper
