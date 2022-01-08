import json

def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")
#
#intro("Read and write task")
#
#def write_it():
#    with open("myfile.txt", "a") as content:
#        x = input("What would you like to write?")
#        content.write("\n" + x)
#        print(f"You have saved: {x}")
#
#def read_it():
#    with open("myfile.txt") as book:
#        for item in book:
#            print(item)
#
#print("What would you like to do?")
#misson = input("Read (r) or Write (w)")
#
#while True:
#    if misson == "r":
#        read_it()
#        break
#    elif misson == "w":
#        write_it()
#        break
#    else:
#        misson = input("The answer must be (r) or (w)")
#
intro("PHONEBOOK")

class Contact:
    def __init__(self, firstname, lastname, phonenumber, city="Unknown"):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.phonenumber = phonenumber
        self.city = city
    
    def __str__(self) -> str:
        return self.fullname

    def __repr__(self) -> str:
        return f"<Name={self.fullname} phonenumber={self.phonenumber} city={self.city}>"
    



class Phonebook:
    def __init__(self, contactlist=None):
        self.contactlist = {} if contactlist is None else contactlist

    def addcontact(self, contact):
        if isinstance(contact, Contact) == True:
            self.contactlist.update({contact.phonenumber:[contact.fullname, contact.firstname, contact.lastname, contact.phonenumber, contact.city]})
        else:
            a = input("Firstname: ")
            b = input("Lastname: ")
            c = int(input("Phonenumber: "))
            d = input("City: ")
            newcontact = Contact(a, b, c, d)
            self.contactlist.update({newcontact.phonenumber:[newcontact.fullname, newcontact.firstname, newcontact.lastname, newcontact.phonenumber, newcontact.city]}



book1 = Phonebook()
book1.addcontact("Rikard")




