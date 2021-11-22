def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("Read and write task")

def write_it():
    with open("myfile.txt", "a") as content:
        x = input("What would you like to write?")
        content.write(content)
        print(f"You have saved: {x}")

def read_it():
    with open("myfile.txt") as book:
        print(book.read())

print("What would you like to do?")
misson = input("Read (r) or Write (w)")

while True:
    if misson == "r":
        read_it()
        break
    elif misson == "w":
        write_it()
        break
    else:
        misson = input("The answer must be (r) or (w)")

