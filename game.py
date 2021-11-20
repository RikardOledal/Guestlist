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

print("Here are your choises")
race = ["Human", "Dwarf", "Elf"]
for item in race:
    print(item)
print("FUNKA")