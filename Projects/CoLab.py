#If some of the rules' checks returns False,
# the function should return False and print
# the reason it failed; otherwise, return the result.
def arg_rules(type_: type, max_length: int, contains: list):
    def inner (func):
        def wrapper (value, *args, **kwargs,):
            if type (value) != type_ :
                print("The argument of the '{}' function should be '{}' only! but '{}' got".format(
                    func.__name__,
                    type_,
                    type(value)
                ))
                return False
            if len (value) > max_length:
                print("First argument of the '{}' function should be less then '{}' chars, but '{}' got.".format(
                    func.__name__,
                    max_length,
                    len(value)
                    ))
                return False
            a = True
            b = str()
            for x in contains:
                if x not in (value):
                    a = False
                    b = x
            if a == False:
                print("The list of the '{}' function should contain {} chars, but doesn't.".format(
                    func.__name__,
                    b,))
                return False
            return func (value, *args, ** kwargs)
        return wrapper
    return inner
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print(create_slogan(12))

