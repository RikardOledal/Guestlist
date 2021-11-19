def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

def make_country(land):
    print ("{} is the capital of {}".format(land["capital"] , land["name"]))

land = input("Country:")
capitol = input("Capitol:")

dict_1 = {
    "name": land,
    "capital": capitol
    "Population": 1000000
}

finland = {
    "name": "Finland",
    "capital": "Helsingfors"
}

make_country(dict_1)