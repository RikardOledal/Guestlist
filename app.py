import json

def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

def readfile(): 
    with open("rikardphonebook.json", "r") as thefile:
        pho_book = json.load(thefile)
        return pho_book

def savefile(var):
    with open("rikardphonebook.json", "w") as thefile:
        json.dump(var, thefile)

def printuser(a):
    print(a.get("full_name"))
    print(a.get("phone_nr"))
    print(a.get("city"))
    print("\n")

intro("PHONEBOOK")

while True:
    print("Your searchoptions are:")
    print("1. Search by first name") 
    print("2. Search by last name")
    print("3. Search by full name")
    print("4. Search by telephone number")
    print("5. Search by city")
    search_nr = input("What kind of search do you want to do?")
    try:
        search_nr = int(search_nr)
    except ValueError:
        search_nr = input("The choise must be a number from 1-5")
        continue
    search_nr = int(search_nr)
    if search_nr == 1:
        search_inp = input("What is the name you want to search for?")
        pho_book = readfile()
        for a, b in pho_book.items():
            if b.get("first_name") == search_inp:
                printuser(b)
        newsearch = input("Do you want to do en new search? (y or n)")
        if newsearch == "n":
            print("ok bye")
            break
    elif search_nr == 2:
        search_inp = input("What is the name you want to search for?")
        pho_book = readfile()
        for a, b in pho_book.items():
            if b.get("last_name") == search_inp:
                printuser(b)
    elif search_nr == 3:
        search_inp = input("What is the name you want to search for?")
        pho_book = readfile()
        for a, b in pho_book.items():
            if b.get("full_name") == search_inp:
                printuser(b)
    elif search_nr == 4:
        search_inp = input("What is the phonenumber you want to search for?")
        pho_book = readfile()
        for a, b in pho_book.items():
            if b.get("phone_nr") == search_inp:
                printuser(b)
    elif search_nr == 5:
        search_inp = input("What is the city you want to search for?")
        pho_book = readfile()
        for a, b in pho_book.items():
            if b.get("city") == search_inp:
                printuser(b)
    else:
        print("Wrong nr")
        break