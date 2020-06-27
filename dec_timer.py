import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time() -start_time
        print('Finished {} in {:.2f} secs'.format(func.__name__, end_time))
        return value
    return wrapper_timer