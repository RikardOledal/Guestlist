# Task 1 - The greatest number
import random
number_list = [random.randint(1,100)]
list_length = len(number_list)
while list_length < 9:
    list_length = len(number_list)
    number_list.append(random.randint(1,100))
print(f"The biggest number in the list are {max(number_list)}")
