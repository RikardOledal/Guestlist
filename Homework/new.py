def add_five(x):
    return x + 5

def do_twice(f):
    def resulting_func(x):
        return f(f(x))
    return resulting_func

result = do_twice(add_five)
print(type(result))
print(result(5))

a = add_five(0)
print(a)