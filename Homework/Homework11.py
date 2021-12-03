#def intro(task):
#    title = f" ** {task} ** "
#    print ("\n")
#    print ("*" * len(title))
#    print (title)
#    print ("*" * len(title))
#    print ("\n")
#
#intro("School")
#
#class Person:
#    def __init__(self, firstname, lastname, age, phone, email=None):
#        self.firstname = firstname
#        self.lastname = lastname
#        self.age = age
#        self.phone = phone
#        self.email = email
#        if isinstance(firstname, str) == False:
#            raise ValueError("Lirstname should be a sting")
#        if isinstance(lastname, str) == False:
#            raise ValueError("Lastname should be a sting")
#        if isinstance(age, int) == False:
#            raise ValueError("Age should be a integrer")
#        if isinstance(phone, int) == False and phone[0-2] == 467 and len(phone) == 11:
#            raise ValueError("Age should be a 11 figure integrer that starts with 467")
#        if email == None:
#            self.email = str.lower(firstname) + "." + str.lower(lastname) + "@school.se"
#        
#    def sinfo(self):
#        print("Name: " + self.firstname + " " + self.lastname)
#        print(f"Age: {self.age}")
#        print(f"Phone: {self.phone}")
#        print("Email: " + self.email + "\n")
#        
#
#class Student(Person):
#    def __init__(self, firstname, lastname, age, phone, email=None, year=1 , grade=3, status="In school"):
#        super().__init__(firstname,lastname,age,phone,email)
#        self.year = year
#        self.grade = grade
#        self.status = status
#
#    def longinfo(self):
#        print("Name: " + self.firstname + " " + self.lastname)
#        print("Status: " + self.status)
#        print(f"Age: {self.age}")
#        print(f"Phone: {self.phone}")
#        print("Email: " + self.email)
#        print(f"Grade: {self.grade}")
#        print(f"Year in school: {self.year}\n")
#
#
#class Teacher(Person):
#    def __init__(self, firstname, lastname, age, phone, salary, hired, email=None):
#        super().__init__(firstname,lastname,age,phone,email)
#        self.salary = salary
#        self.hired = hired
#
#    def longinfo(self):
#        print("Name: " + self.firstname + " " + self.lastname)
#        print(f"Age: {self.age}")
#        print(f"Phone: {self.phone}")
#        print("Email: " + self.email)
#        print(f"Salary: ${self.salary}")
#        print(f"Hired: {self.hired}\n")
#
#kalle = Person("Carl", "Forsudd", 8, 46749658745)
#
#karin = Student("Karin", "Petersson", 7, 46778934562)
#
#kajsa = Teacher("Kajsa", "Berggren", 42, 4678945645656, 12800, 1989)
#
#kajsa.sinfo()
#
#karin.sinfo()
#
#kajsa.longinfo()
#
#karin.longinfo()
#
#intro("Mathematician")
#
#class Mathematician:
#    def square_nums(self, nums):
#        if isinstance(nums, list) == False:
#            raise ValueError("nums should be a list")
#        return [n**2 for n in nums]
#    
#    def remove_positives(self, nums):
#        if isinstance(nums, list) == False:
#            raise ValueError("nums should be a list")
#        return [n for n in nums if n > 0]
#    
#    def filter_leaps(self, nums):
#        if isinstance(nums, list) == False:
#            raise ValueError("nums should be a list")
#        return [n for n in nums if (n % 100 != 0 and n % 4 == 0) or (n % 100 == 0 and n % 400 == 0)]   
#
#m = Mathematician()
#
#while True:
#    print("1. Square numbers")
#    print("2. Remove positives")
#    print("3. Filter leaps")
#    print("4. Exit")
#    print("\n")
#    choise = input("What would you like to do? (1-4)")
#    try:
#        int(choise)
#    except ValueError:
#        print("Choise must be a number 1-3")
#    else:
#        choise = int(choise)
#    if choise == 4:
#        print("Ok. Bye!!!")
#        break
#    if choise < 1 or choise > 4:
#        print("Invalid choise")
#        continue
#    numbers = []
#    x = input("What number do you want to add?")
#    while x != "n":
#        try:
#            int(x)
#        except ValueError:
#            x = input("What number do you want to add? (n to stop adding)")
#            continue
#        else:
#            x = int(x)
#            numbers.append(x)
#            x = input("What number do you want to add? (n to stop adding)")
#    if choise == 1:
#        print(numbers)
#        print(m.square_nums(numbers))
#    elif choise == 2:
#        print(numbers)
#        print(m.remove_positives(numbers))
#    elif choise == 3:
#        print(numbers)
#        print(m.filter_leaps(numbers))
#    else:
#        print("Invalid choise")
#
#intro("Product Store")

productlist = []

class Product:
    def __init__(self, type, name, price) -> None:
        if isinstance(type, str) == True and isinstance(name, str) == True:
            type = str.title(type)
            name = str.title(name)
        else:
            raise ValueError("Type och Name should be str")
        if not isinstance(price, int):
            raise ValueError("Price should be int")
        self.type = type # The products salescategory
        self.name = name # The name of the Product
        self.price = price # The price of the Product

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"
    
    def __repr__(self) -> str:
        return f"{self.name} {self.type} {self.price}\n"
    


class ProductStore:
    def __init__(self, prices=None, sales=None, store=None, discounts=None):
        self.prices = {}
        self.sales = {}
        self.discounts = {}
        self.stock = {}
        self.all_prod = {
            "Appel" : Product("Fruit", "Appel", 5),
            "Orange" : Product("Fruit", "Orange", 7),
            "Pear" : Product("Fruit", "Pear", 6),
            "Lemon" : Product("Fruit", "Lemon", 5), 
            "Banana" : Product("Fruit", "Banana", 3),
            "Tennisball" : Product("Sport", "tennisball", 10),
            "Basketball" : Product("Sport", "basketball", 20),
            "Tennisracket" : Product("Sport", "tennisracket", 250),
            "Flippers" : Product("Sport", "flippers", 150),
            "Swimsuit" : Product("Sport", "swimsuit", 100),
            "Fotball" : Product("Sport", "Fotball", 30),
            "Milk" : Product("Dairies", "milk", 9),
            "Yoghurt" : Product("Dairies", "Yoghurt", 15),
            "Creme fraiche" : Product("Dairies", "Creme fraiche", 9),
            "Whipped cream" : Product("Dairies", "Whipped cream", 12),            
        }
    def addproduct(typ, nam, pric):
        self.all_prod.update({typ : Product(typ, nam, pric)})

    def add(self, prod, amount):
        self.prod = prod
        self.amount = amount
        if prod.name in self.stock:
            addition = amount + self.stock[prod.name]
            self.stock.update({prod.name:addition})
        else:
            self.stock.update({prod.name:amount})
            self.prices.update({prod.name:prod.price})
            self.sales.update({prod.name:0})
            self.discounts.update({prod.name:0})
        if prod.type not in self.discounts:
            self.discounts.update({prod.type:0})

        # adds a specified quantity of a single product with a predefined price premium for your store(30 percent)

    def set_discount(self, identifier, percent, identifier_type):
        # adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
        pass

    def sell_product(self, product_name, amount):
        # Removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
        pass

    def get_income(self):
        # returns amount of many earned by ProductStore instance.
        pass

    def get_all_products():
        # Returns information about all available products in the store.
        pass

    def get_product_info(product_name):
        # returns a tuple with product name and amount of items in the store.
        pass

#all_prod = {
#    "appel" : Product("Fruit", "Appel", 5),
#    "appel" : Product("Fruit", "Appel", 5),
#    "orange" : Product("Fruit", "Orange", 7),
#    "pear" : Product("Fruit", "Pear", 6),
#    "lemon" : Product("Fruit", "Lemon", 5), 
#    "banana" : Product("Fruit", "Banana", 3),
#    "tennisball" : Product("Sport", "tennisball", 10),
#    "basketball" : Product("Sport", "basketball", 20),
#    "tennisracket" : Product("Sport", "tennisracket", 250),
#    "flippers" : Product("Sport", "flippers", 150),
#    "swimsuit" : Product("Sport", "swimsuit", 100),
#    "fotball" : Product("Sport", "Fotball", 30),
#    "milk" : Product("Dairies", "milk", 9),
#    "yoghurt" : Product("Dairies", "Yoghurt", 15),
#    "creme fraiche" : Product("Dairies", "Creme fraiche", 9),
#    "whipped cream" : Product("Dairies", "Whipped cream", 12),
#}

#appel = Product("Fruit", "Appel", 5)
#orange = Product("Fruit", "Orange", 7)
#pear = Product("Fruit", "Pear", 6)
#lemon = Product("Fruit", "Lemon", 5) 
#banana = Product("Fruit", "Banana", 3)
#tennisball = Product("Sport", "tennisball", 10)
#basketball = Product("Sport", "basketball", 20)
#tennisracket = Product("Sport", "tennisracket", 250)
#flippers = Product("Sport", "flippers", 150)
#swimsuit = Product("Sport", "swimsuit", 100)
#fotball = Product("Sport", "Fotball", 30)
#milk = Product("Dairies", "milk", 9)
#yoghurt = Product("Dairies", "Yoghurt", 15)
#cremefraiche = Product("Dairies", "Creme fraiche", 9)
#whippedcream = Product("Dairies", "Whipped cream", 12)

rikardstore = ProductStore()

while True:
    print("\n")
    print("1. Add products")
    print("2. Set discount")
    print("3. Sell product")
    print("4. Get income")
    print("5. Storage")
    print("6. Storage info")
    print("7. Exit")
    print("\n")
    option = input("What would you like to do? (1-8)")
    try:
        int(option)
    except ValueError:
        pass
    else:
        option = int(option)
    if option == 1:
        prd = input("What would you like to add?")
        amn = input("How many would you like to add?")
        try:
            int(amn)
        except ValueError:
            break
        else:
            if prd in rikardstore.all_prod:
                rikardstore.add(rikardstore.all_prod[prd],amn)
                print(f"You have added {amn} {prd}")
            else:
                prd_typ = input(f"What kind of type is {prd}?")
                prd_pri = input(f"What is the price of {prd}?")
                try:
                    int(prd_pri)
                except ValueError:
                    break
                else:
                    prd_pri = int(prd_pri)
                    rikardstore.all_prod.update({prd : Product(prd_typ, prd, prd_pri)})
                    rikardstore.add(rikardstore.all_prod[prd],amn)
                else:
                    break
    elif option == 2:
        a = input("What would you like to add?")
        b = input("How many would you like to add?")
        c = input("How many would you like to add?")
    elif option == 3:
        print(rikardstore.all_prod.values())
    elif option == 4:
        pass
    elif option == 5:
        print(rikardstore.stock)
    elif option == 6:
        pass
    elif option == 7:
        print("System shutting down!")
        break
    else:
        print("Choise should be a number between 1 and 8")