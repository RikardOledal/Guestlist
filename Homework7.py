def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("Simple function")

def favorite_movie(name):
    print (f"My favorite movie is named {name}")

favorite_movie("Batman")

intro("Creating a dictionary")

def make_country(land):
    print ("{} is the capital of {}".format(land["capital"] , land["name"]))

sweden = {
    "name": "Sweden",
    "capital": "Stockholm"
}

make_country(sweden)

intro ("The calculator")

def make_operation (opr, number, *args):
    awnser = number
    for i in args:
        if opr == "+":
            awnser += i
        elif opr == "-":
            awnser -= i
        elif opr == "*":
            awnser *= i
    print(awnser)

make_operation("*", 2, 5, 10)


