import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
        finally:
            end = time.time()
            print(f"{func.__name__} executed in {end - start:.4f} seconds")
    return wrapper