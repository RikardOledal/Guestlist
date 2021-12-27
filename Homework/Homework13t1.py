def favorite_movie(name, year, director):
    print (f"My favorite movie is named {name} from {year} by {director}")

def make_country(capitol, land):
    print (f"{capitol} is the capital of {land}")

def local_var(func):
    print(f"The {func.__name__}-function contains {func.__code__.co_nlocals} local varibles")

local_var(favorite_movie)
local_var(make_country)