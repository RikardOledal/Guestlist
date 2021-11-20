import pprint

def newstage(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

gamename = "ROLEPLAY"

newstage(gamename)

print(f"Welcome to the world of {gamename}")
print("Let´s start by creating your chacter")

def chooselist(alternatives):
    print("Your options are")
    for i in alternatives:
        print("{a}. {b}".format(a=i, b=alternatives[i]))
    choise = input("Make your choise!")
    print(choise)

race =["Dwarf", "Elf", "Human"]

chooselist(race)




