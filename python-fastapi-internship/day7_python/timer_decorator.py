import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Time taken: {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def count_to_million():
    for i in range(1_000_000):
        pass


count_to_million()