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

def chooselist(alt):
    print("@"*30)
    print("@@ Your choises are         @@")
    print("@@                          @@")
    x = 0
    for item in alt:
        x += 1
        print(f"@@ {x}. {item} "+" "*(22-len(item)-len(str(x)))+"@"*2)
    print("@"*30)
    choise = input("Make your choise! (just the number)")
    return choise

if chooselist(race):


