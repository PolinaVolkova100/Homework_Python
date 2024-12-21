import time
from datetime import timedelta


def retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exception)] = (Exception,)):  # type: ignore
    if count < 1:
        raise ValueError
    def decorator_retry(func):
        def wrapper(*args, **kwargs):
            attempt, result = 0, None
            while attempt < count:
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as err:
                    result = err
                    if attempt != count - 1:
                        time.sleep(delay.total_seconds())
                attempt += 1
            raise result
        return wrapper
    return decorator_retry


