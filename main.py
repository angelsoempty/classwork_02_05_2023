def decorator_cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@decorator_cache
def fun(x, y):
    return x * y

print(fun(3,10))
