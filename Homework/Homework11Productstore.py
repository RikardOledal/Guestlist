import json
from typing import Type

def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("Product Store")

with open("storeproducts.json", "r") as file1:
    productlist = json.load(file1)
with open("storeincome.json", "r") as file2:
    incomelist = json.load(file2)
with open("storeprices.json", "r") as file3:
    priceslist = json.load(file3)
with open("storestock.json", "r") as file4:
    stocklist = json.load(file4)

discountlisttypes = {
    "Fruit" : 0,
    "Sport" : 0,
    "Dairies" : 0,
}

discountlistproducts = {
    "Apple": 0,
    "Pear": 0,
}

class Product:
    def __init__(self, type, name, price):
        if isinstance(type, str) == True and isinstance(name, str) == True:
            type = str.title(type)
            name = str.title(name)
        else:
            raise ValueError("Type och Name should be str")
        if isinstance(price, int) == False:
            raise ValueError("Price should be int")
        self.type = type # The products salescategory
        self.name = name # The name of the Product
        self.price = price # The price of the Product

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"
    
    def __repr__(self):
        return f"{self.name} {self.type} {self.price}\n"

class ProductStore:
    def __init__(self):
        self.income = incomelist
        self.prices = priceslist
        self.discounts = {}
        self.stock = stocklist
        self.all_prod = productlist

    def add(self, prod, amount):
        self.prod = str.title(prod)
        self.amount = int(amount)
        if prod in stocklist:
            addition = amount + stocklist[prod]
            stocklist.update({prod:addition})
        else:
            # Add product
            price = input(f"What is the price for {prod}")
            while isinstance(price, int) == False:
                try:
                    int(price)
                except ValueError:
                    price = input("Price should be a positive number. Please try agian.")
                else:
                    price = int(price)
            categori = input(f"What is the category for {prod}")
            # Add to productlist
            productlist.update({prod : [categori, price]})
            # Add to stock
            stocklist.update({prod : amount})
            # Add to income
            incomelist.update({prod : 0})
            # Add to prices
            storeprice = price*1.3
            priceslist.update({prod : storeprice})
            # Add to discount
            
        # adds a specified quantity of a single product with a predefined price premium for your store(30 percent)

    def set_discount(self, identifier, percent, identifier_type):
        # adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
        pass

    def sell_product(self, product_name, amount):
        self.product_name = str.title(product_name)
        while isinstance(amount, int) == False:
            try:
                int(amount)
            except ValueError:
                amount = input("The amoont should be a positive number. Please try agian.")
            else:
                amount = int(amount)
        self.amount = amount
        if product_name in stocklist and amount<=stocklist[product_name]:
            price = priceslist[product_name]
            if product_name in discountlist:
                price = price*(discountlist[product_name]/100)
            for k, v in productlist.items():
                if k == product_name:
                    category = v[0]3
            if category in discountlist:
                price = price*(discountlist[category]/100)
            income = round((amount * priceslist[product_name]), 2)
            incomeuppdate = income + incomelist[product_name]
            incomelist.update({product_name:incomeuppdate})
            sell = stocklist[product_name] - amount
            stocklist.update({product_name:sell})
            print("You sold {} {} for {} kr".format(amount, product_name, income))
        elif product_name in stocklist and amount>stocklist[product_name]:
            print("You tried to sell {} {} when you only have {}".format(amount, product_name, stocklist[product_name]))
        else:
            print(f"You don´t own any {product_name} in you stock")

        # Removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.

    def get_income(self):
        # returns amount of many earned by ProductStore instance.
        pass

    def get_all_products():
        # Returns information about all available products in the store.
        pass

    def get_product_info(product_name):
        # returns a tuple with product name and amount of items in the store.
        pass

    def incomelist(self):
        return self.income

    def stocklist(self):
        return self.stock
    
    def priceslist(self):
        return self.prices

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
        while isinstance(amn, int) == False:
            try:
                int(amn)
            except ValueError:
                amn = input("How many would you like to add?")
            else:
                amn = int(amn)
                rikardstore.add(prd, amn)
    elif option == 2:
        a = input("What would you like to add?")
        b = input("How many would you like to add?")
        c = input("How many would you like to add?")
    elif option == 3:
        prd = input("What would you like to sell?")
        amn = input("How many would you like to sell?")
        rikardstore.sell_product(prd, amn)
        print(rikardstore.income)
    elif option == 4:
        pass
    elif option == 5:
        print(rikardstore.stock)
    elif option == 6:
        pass
    elif option == 7:
        with open("storeproducts.json", "w") as file1:
            json.dump(productlist, file1)
        with open("storeincome.json", "w") as file2:
            json.dump(incomelist, file2)
        with open("storeprices.json", "w") as file3:
            json.dump(priceslist, file3)
        with open("storestock.json", "w") as file4:
            json.dump(stocklist, file4)
        print("System shutting down!")
        break
    else:
        print("Choise should be a number between 1 and 8")