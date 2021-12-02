def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("School")

class Person:
    def __init__(self, firstname, lastname, age, phone, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.phone = phone
        self.email = email
        if isinstance(firstname, str) == False:
            raise ValueError("Lirstname should be a sting")
        if isinstance(lastname, str) == False:
            raise ValueError("Lastname should be a sting")
        if isinstance(age, int) == False:
            raise ValueError("Age should be a integrer")
        if isinstance(phone, int) == False and phone[0-2] == 467 and len(phone) == 11:
            raise ValueError("Age should be a 11 figure integrer that starts with 467")
        if email == None:
            self.email = str.lower(firstname) + "." + str.lower(lastname) + "@school.se"
        
    def sinfo(self):
        print("Name: " + self.firstname + " " + self.lastname)
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print("Email: " + self.email + "\n")
        

class Student(Person):
    def __init__(self, firstname, lastname, age, phone, email=None, year=1 , grade=3, status="In school"):
        super().__init__(firstname,lastname,age,phone,email)
        self.year = year
        self.grade = grade
        self.status = status

    def longinfo(self):
        print("Name: " + self.firstname + " " + self.lastname)
        print("Status: " + self.status)
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print("Email: " + self.email)
        print(f"Grade: {self.grade}")
        print(f"Year in school: {self.year}\n")


class Teacher(Person):
    def __init__(self, firstname, lastname, age, phone, salary, hired, email=None):
        super().__init__(firstname,lastname,age,phone,email)
        self.salary = salary
        self.hired = hired

    def longinfo(self):
        print("Name: " + self.firstname + " " + self.lastname)
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print("Email: " + self.email)
        print(f"Salary: ${self.salary}")
        print(f"Hired: {self.hired}\n")

kalle = Person("Carl", "Forsudd", 8, 46749658745)

karin = Student("Karin", "Petersson", 7, 46778934562)

kajsa = Teacher("Kajsa", "Berggren", 42, 4678945645656, 12800, 1989)

kajsa.sinfo()

karin.sinfo()

kajsa.longinfo()

karin.longinfo()

intro("Mathematician")

class Mathematician:
    def square_nums(self, nums):
        if isinstance(nums, list) == False:
            raise ValueError("nums should be a list")
        return [n**2 for n in nums]
    
    def remove_positives(self, nums):
        if isinstance(nums, list) == False:
            raise ValueError("nums should be a list")
        return [n for n in nums if n > 0]
    
    def filter_leaps(self, nums):
        if isinstance(nums, list) == False:
            raise ValueError("nums should be a list")
        return [n for n in nums if (n % 100 != 0 and n % 4 == 0) or (n % 100 == 0 and n % 400 == 0)]   

m = Mathematician()

while True:
    print("1. Square numbers")
    print("2. Remove positives")
    print("3. Filter leaps")
    print("4. Exit")
    print("\n")
    choise = input("What would you like to do? (1-4)")
    try:
        int(choise)
    except ValueError:
        print("Choise must be a number 1-3")
    else:
        choise = int(choise)
    if choise == 4:
        print("Ok. Bye!!!")
        break
    if choise < 1 or choise > 4:
        print("Invalid choise")
        continue
    numbers = []
    x = input("What number do you want to add?")
    while x != "n":
        try:
            int(x)
        except ValueError:
            x = input("What number do you want to add? (n to stop adding)")
            continue
        else:
            x = int(x)
            numbers.append(x)
            x = input("What number do you want to add? (n to stop adding)")
    if choise == 1:
        print(numbers)
        print(m.square_nums(numbers))
    elif choise == 2:
        print(numbers)
        print(m.remove_positives(numbers))
    elif choise == 3:
        print(numbers)
        print(m.filter_leaps(numbers))
    else:
        print("Invalid choise")
    