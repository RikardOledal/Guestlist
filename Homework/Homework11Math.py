def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

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