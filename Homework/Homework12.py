def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

# intro("Method overloading")
# 
# class Animal:
#     def __init__(self, legs, age):
#         self.legs = str(legs)
#         self.age = int(age)
#     def talk(self):
#         print("Animals don´t speak!!!")
# 
# class Dog(Animal):
#     def __init__(self, race, age, legs=4):
#         super().__init__(legs, age)
#         self.race = race
#     
#     def talk(self):
#         print("Bow wow")
# 
# class Cat(Animal):
#     def __init__(self, race, age, legs=4):
#         super().__init__(legs, age)
#         self.race = race
# 
#     def talk(self):
#         print("Meow")
# 
# fido = Dog("Jack russel", age=3)
# musse = Cat("Siames", age=2)
# while True:
#     print("1. Fido is a dog")
#     print("2. Musse is a cat")
#     print("3. Exit")
#     call = input("Who you wanna call?")
#     if str.lower(call) == "fido" or call == "1":
#         fido.talk()
#     elif str.lower(call) == "musse" or call == "2":
#         musse.talk()
#     elif str.lower(call) == "exit" or call == "3":
#         print("Okej bye!")
#         break
#     else:
#         print("That's not an option!!!")






intro("A Person class")

class Author:
    def __init__(self, name, country, birthday:int, books = []):
        self.name = name
        self.country = country
        try:
            if len(birthday) != 8:
                raise ValueError("Birthday shold be 8 numbers.")
        self.birthday = birthday
        self.books = books

class Book:
    def __init__(self, name, year, author:Author):
    pass

class Library:
    def __init__(self, name, books = [], authors = []):
        pass

eddings = Author("David Eddings", "England", "Wensday", [])