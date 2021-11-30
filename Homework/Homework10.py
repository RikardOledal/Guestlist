def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("A Person class")

class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def talk(self):
        firstname = self.firstname
        lastname = self.lastname
        age = self.age
        print(f"Hello, my name is {firstname} {lastname} and my age are {age}")

rikard = Person("Rikard", "Oledal", 40)
johan = Person("Johan", "Engman", 35)

rikard.talk()
johan.talk()

intro("Doggy age")

class Dog():
    def __init__(self, name, race, age=1):
        if isinstance(age, int) == False or age < 0:
            raise ValueError("Age should be a positive number")
        self.name = name
        self.race = race
        self.age = age

    def dogyears(self):
        dogage = self.age * 7
        return dogage

platon = Dog("Platon", "Terrier", 4)

print(f"{platon.name} is {platon.dogyears()} in dogyears")

intro("TV controller")

class controller():
    def __init__(self, channels):
        if isinstance(channels, list) == False:
            raise ValueError("Channels should be a list")
        self.channels = channels
        self.ondisplay = 0

    def menu(self):
        print("1. First channel")
        print("2. Last channel")
        print("3. Previos channel")
        print("4. Next channel")
        print("5. Choose channel")
        print("6. List Channels")
        print("7. Add Channel")
        print("8. Turn TV off")

    def current_channel(self):
        return self.channels[self.ondisplay]

    def next_channel(self):
        if self.ondisplay == len(self.channels)-1:
            self.ondisplay = 0
        else:
            self.ondisplay += 1

    def previous_channel(self):
        if self.ondisplay == 0:
            self.ondisplay = len(self.channels)-1
        else:
            self.ondisplay -= 1
    
    def first_channel(self):
        self.ondisplay = 0

    def last_channel(self):
        self.ondisplay = len(self.channels)-1

    def turn_channel(self, pickone):
        self.pickone = pickone
        if pickone <= len(self.channels) and pickone >= 1:
            self.ondisplay = pickone - 1
        else:
            print("Channelchoise must be a number from 1 to {}".format(len(self.channels)))




    def listchannels(self):
        for c in self.channels:
            print("Channel {} : {}".format(self.channels.index(c)+1, c))
    
    def addchannel(self, newchannel):
        self.channels.append(newchannel)
        print("{} was added at channel {}".format(newchannel, self.channels.index(newchannel)+1))

chan = ["BBC", "Discovery", "TV1000"]
tv = controller(chan)

print(tv.listchannels())

while True:
    print("\n")
    print(f"You are now watching {tv.current_channel()}\n")
    tv.menu()
    tvoption = input("\n What do you want to do? (1-8)")
    if tvoption == "1":
        tv.first_channel()
    elif tvoption == "2":
        tv.last_channel()
    elif tvoption == "3":
        tv.previous_channel()
    elif tvoption == "4":
        tv.next_channel()
    elif tvoption == "5":
        tv.listchannels()
        choose_chan = input("What do you want to watch?")
        try:
            int(choose_chan)
        except ValueError:
            print("Must be a number between 1 and {}".format(len(tv.channels)))
        else:
            choose_chan = int(choose_chan)
            tv.turn_channel(choose_chan)
    elif tvoption == "6":
        tv.listchannels()
    elif tvoption == "7":
        addone = input("What channel would you like to add?")
        tv.addchannel(addone)
    elif tvoption == "8":
        print("You have turned off the TV")
        break
    else:
        print("Invalid choise. Must be a number from 1-6")






