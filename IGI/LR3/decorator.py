import time

def timer_decorator(func):
    """
    Decorator for measuring function execution time.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of the function {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper