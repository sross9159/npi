import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return value, execution_time
    return wrapper

