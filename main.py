#теорія Декоратори

def my_decorator_func(func): #3
    def wrapper(): #4
        print('shoto tam')
        func()
        print('i tam shos')
    return wrapper


@my_decorator_func #2
def say_hello(): #1
    print('Hello!')
say_hello()