'''Task 1

Write a decorator that prints a function with arguments passed to it.

It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"'''

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        listargs = [a for a in args]
        listkwargs = kwargs.items()
        listkwargs = list(listkwargs)
        all = listargs + listkwargs
        print(all)
        print(f"{func.__name__} with {all} resulted in {result}")
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

def testfunc(number, dog):
    return [number, dog]

print(add(6, 9))
print(square_all(6, 9))

