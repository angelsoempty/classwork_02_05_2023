def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Call: {func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper

@log
def my_function(x, y):
    return x + y

my_function(5, 3)
my_function(2, 7)