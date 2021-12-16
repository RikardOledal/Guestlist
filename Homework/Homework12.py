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

intro("A Library")

class Author:
    def __init__(self, name, country, birthday, books=None):
        if type(name) is not str:
            raise ValueError("Name should be str")
        if type(country) is not str:
            raise ValueError("Country should be str")
        if type(birthday) is not int:
            raise ValueError("Birthday should be int")
        if len(str(birthday)) != 8:
            raise ValueError("Birthday should be 8 numbers: YYYYMMDD")
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = [] if books is None else books

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def info(self):
        return "Author: {}\nCountry: {}\nBirthday: {}-{}-{}\nBooks: {}\n".format(self.name, self.country, str(self.birthday)[0:4], str(self.birthday)[4:6], str(self.birthday)[6:8], self.books)


class Book:
    def __init__(self, name, year, author):
        if type(name) is not str:
            raise ValueError("Name should be str")
        if type(year) is not int:
            raise ValueError("Year should be int")
        if len(str(year)) != 4:
            raise ValueError("Year should be 4 numbers")
        if not isinstance(author, Author):
            raise ValueError("Athor should be Class Author")
        self.name = name
        self.year = year
        self.author = author
    
    def __str__(self):
        return self.name

    def info(self):
        return "Book: {}\nAuthor: {}\nYear: {}\n".format(self.name, self.author, self.year)


class Library:
    def __init__(self, name, books = None, authors = None):
        if type(name) is not str:
            raise ValueError("Name should be str")
        if not books == None:
            if not type(books) is list:
                raise ValueError("Books should be None or a list")
        if not authors == None:
            if not type(authors) is list:
                raise ValueError("Authors should be None or a list")
        self.name = name
        self.books = [] if books is None else books
        self.authors = [] if authors is None else authors

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def info(self):
        return "Name: {}\nAuthors: {}\nBooks: {}\n".format(self.name, len(self.authors), len(self.books))
    
    def new_book(self, name, year, author):
        if type(name) is not str:
            raise ValueError("Name should be str")
        if type(year) is not int:
            raise ValueError("Year should be int")
        if len(str(year)) != 4:
            raise ValueError("Year should be 4 numbers")
        if not isinstance(author, Author):
            raise ValueError("Athor should be Class Author")
        book = Book(name, year, author)
        self.books.append(book)
        if not author in self.authors:
            self.authors.append(author)
        return book
    
    def group_by_author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Athor should be Class Author")
        return filter(lambda book: book.author == author, self.authors)

    def group_by_year(self, year):
        if type(year) is not int:
            raise ValueError("Year should be int")
        return filter(lambda book: book.year == year, self.books)
        
    


eddings = Author("David Eddings", "England", 19310707, ["Pawn of Prophecy", "Queen of Sorcery", "Magician's Gambit"])
jordan = Author("Robert Jordan", "USA", 19481017)
pawn = Book("Pawn of Prophecy", 1982, eddings)
huddinge = Library("Huddinge bibliotek")

print(eddings)
print(eddings.info())
print("\n")
print(huddinge)
print(huddinge.info())
print("\n")
print(huddinge.new_book("Queen of Sorcery", 1982, eddings))
print("\n")
print(huddinge.info())
print(huddinge.new_book("Pawn of Prophecy", 1982, eddings))
print("\n")
print(huddinge.info())
print("\n")
print(huddinge.new_book("The Eye of the World", 1990, jordan))
print("\n")
print(huddinge.info())
print(huddinge.group_by_author(jordan))
print(huddinge.group_by_year(1990))





