import time
import functools
import logging


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round((time.time() - start_time) * 1000, 2)
        logging.info(f"{func.__name__} executed in {execution_time} ms")
        return result
    return wrapper


def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception("Unhandled exception occurred")
            raise e
    return wrapper


def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
