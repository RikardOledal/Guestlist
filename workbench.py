import json

pho_book = {}

def readfile(): 
    with open("rikardphonebook.json", "r") as thefile:
        pho_book = json.load(thefile)
        return pho_book

def savefile(var):
    with open("rikardphonebook.json", "w") as thefile:
        json.dump(var, thefile)

def updatephob(name1, name2, bothname, nr, town):
    pho_book.update({
    nr : {
        "first_name" : name1,
        "last_name" : name2,
        "full_name" : bothname,
        "phone_nr" : nr,
        "city" : town,
    }
})

# ADD USER ########################################
#fname = input("First name: ")
#lname = input("Last name: ")
#fullname = fname + " " + lname
#phonenr = input("Phonenumber: ")
#city = input("City: ")
#
#pho_book = readfile()
#pho_book.update({
#    phonenr : {
#        "first_name" : fname,
#        "last_name" : lname,
#        "full_name" : fullname,
#        "phone_nr" : phonenr,
#        "city" : city,
#    }
#})
#
#savefile(pho_book)
#print("Saved {} with number {}".format(fullname, phonenr))
####################################################

## PRINT LIST #######################################
#pho_book = readfile()
#print(type(pho_book))
#print(pho_book)
#for a, b in pho_book.items():
#    print(b.get("full_name"))
#    print(b.get("phone_nr"))
#    print(b.get("city"))
#    print("\n")
#####################################################



#pho_book = {
#    "0738394420" : {
#        "first_name" : "",
#        "last_name" : "Oledal",
#        "full_name" : "Rikard Oledal",
#        "phone_nr" : "0738394420",
#        "city" : "Upplands vasby",
#    }
#}
#print("\n")
#print(pho_book)
#print("\n")
#
#with open("rikardphonebook.json", "w") as pho_book:
#    json.dump(pho_book, thefile)
fname = input("First name: ")
lname = input("Last name: ")
fullname = fname + " " + lname
phonenr = input("Phonenumber: ")
city = input("City: ")
updatephob(fname, lname, fullname, phonenr, city)

#pho_book = readfile()
#def updatefile(name1, name2, bothname, nr, town):
#    pho_book.update({
#    phonenr : {
#        "first_name" : name1,
#        "last_name" : name2,
#        "full_name" : bothname,
#        "phone_nr" : nr,
#        "city" : town,
#    }
#})


#pho_book.update({
#    phonenr : {
#        "first_name" : fname,
#        "last_name" : lname,
#        "full_name" : fullname,
#        "phone_nr" : phonenr,
#        "city" : city,
#    }
#})
#
savefile(pho_book)
print("Saved {} with number {}".format(fullname, phonenr))
#
##with open("rikardphonebook.json", "w") as thefile:
##    json.dump(pho_book, thefile)
#
#print(pho_book)
#
#for a, b in pho_book.items():
#    print(b.get("full_name"))
#    print(b.get("phone_nr"))
#    print(b.get("city"))
#    print("\n")
#
#with open("rikardphonebook.json", "w") as thefile:
#    json.dump(pho_book, thefile)