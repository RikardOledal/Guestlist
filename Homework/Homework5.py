# Task 1 - The greatest number
import random
number_list = [random.randint(1,100)]
list_length = len(number_list)
while list_length < 9:
    list_length = len(number_list)
    number_list.append(random.randint(1,100))
print(number_list)
print(f"The biggest number in the list are {max(number_list)}")

# Task 2 - Exclusive common numbers.
a_list = [random.randint(1,50)]
b_list = [random.randint(1,50)]
ab_length = len(a_list)
while ab_length < 9:
    ab_length = len(a_list)
    a_list.append(random.randint(1,50))
    b_list.append(random.randint(1,50))
c_list = []
i = 0
while i <= 50:
    if i in a_list and i in b_list:
        c_list.append(i)
    i += 1
print(f"First list was {a_list}")
print(f"Second list was {b_list}")
if c_list == []:
    print("There were no common integers")
else:
    print(f"The common integers are {c_list}")

# Task 3 - Extracting numbers.
hundredlist = [1]
redlist = []
i = 1
while i < 100:
    i += 1
    hundredlist.append(i)
i = 0
while i < len(hundredlist):
    if hundredlist[i] % 7 == 0 and hundredlist[i] % 5 != 0:
        redlist.append(hundredlist[i])
    i += 1
print(f"The numbers from 1-100 that is divideble by 7 and not dividele by 5 is {redlist}")







