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
print("Welcome to the phonebook.")
print ("\n")

while True:
    print("What would you like to do?")
    print("1. Add new contact")
    print("2. Search mode")
    print("3. Delete a contact")
    print("4. Update a contact")
    print("5. Exit the phonebook")
    print ("\n")
    choise = input("Choose a number from 1-6")
    while True:
        try:
            choise = int(choise)
        except ValueError:
            choise = input("The choise must be a number from 1-6")
            continue
        choise = int(choise)
        break
    if choise == 1:
        print("User added")
        fname = input("First name: ")
        lname = input("Last name: ")
        fullname = fname + " " + lname
        phonenr = input("Phonenumber: ")
        city = input("City: ")

        pho_book = readfile()
        pho_book.update({
            phonenr : {
                "first_name" : fname,
                "last_name" : lname,
                "full_name" : fullname,
                "phone_nr" : phonenr,
                "city" : city,
            }
        })

        savefile(pho_book)
        print("Saved {} with number {}".format(fullname, phonenr))
        ###################################################
    elif choise == 2:
        print("Your searchoptions are:")
        print("1. Search by first name") 
        print("2. Search by last name")
        print("3. Search by full name")
        print("4. Search by telephone number")
        print("5. Search by city")
        search_nr = input("What kind of search do you want to do?")
        while True:
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
    elif choise == 3:
        print("What is the phonenumber of the contact you want to delete?")
    elif choise == 4:
        print("What is the phonenumber of the contact you want to update?")
    elif choise == 5:
        print("Welcome back!")
        break
    else:
        print("Invalid entry")