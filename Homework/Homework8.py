def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("OOPS")

def oops():
    raise IndexError

def errorhandler():
    try:
        oops()
    except IndexError:
        print("We got an Indexerror over here")
    finally:
        print("We are done")

intro("zerodivision-handler")

def divide_it():
    a = (input("Give me a number"))
    b = (input("Give me another number"))
    while True:
        try:
            a = float(a)
        except ValueError:
            a = (input("The first value was not a number. Please try again"))
            continue
        try:
            b = float(b)
        except ValueError:
            b = (input("The second value was not a number. Please try again"))
            continue
        try:
            (a*a)/b
        except ZeroDivisionError:
            print("You can't divide by 0")
            break
        else:
            c = (float(a)*float(a))/float(b)
            print(f"({a} * {a}) / {b} = {c}")
            break
divide_it()