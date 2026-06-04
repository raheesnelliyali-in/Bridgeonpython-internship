def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper
@log_call
def add(a, b):
    return a + b
@log_call
def greet(name):
    print(f"Hello {name}")
@log_call
def multiply(x, y):
    return x * y
print(add(10, 20))
greet("Rahees")
print(multiply(5, 4))