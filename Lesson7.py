name = "The functions.py script"

def greet():
    print("Hello, Python World!")

greet()

def calculate_total(amount, discount):
    return amount - (amount*discount)

total =calculate_total(99.99, 0.1)

print(f"Total {total}")

def greet_person(name, age=None):
    print(f"Hello, {name}")
    if age is not None:
        print(f"You are {age} years old")

greet_person("Rikard", 40)
greet_person("Sara")

print(name)

def print_user(user):
    print(f"Name: {user["first_name"]} {user} / Email: {user["email"]}")

anna ={
    "first_name": "Anna",
    "last_name": "Lindstrand",
    "email": "anna.lindstrand@gmail.com"
}

print_user(anna)