def add_numb(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 10
    return wrapper

@add_numb
def number(n):
    return n

print(number(5))
