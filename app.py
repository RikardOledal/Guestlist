import random
# display intro
title = ' ** Math Quiz ** '
print ('*' * len(title))
print (title)
print ('*' * len(title))
# display menu
menu_list = ('1. Addition', '2. Subtraction', '3. Multiplication', '4. Integer Division', '5. Exit')
print (menu_list[0])
print (menu_list[1])
print (menu_list[2])
print (menu_list[3])
print (menu_list[4])
# display_separator
print ('-' * 24)
# user input
options = int(input('input opperator:'))
while options > 5 or options < 1 :
    print ('Invalid menu option.')
    options = int(input('Please try again:'))
# Operations
firstnumber = random.randint(1,100)
secondnumber = random.randint(1,100)
if options == 1 :
    print(f"What is {firstnumber} + {secondnumber}?")
    result = firstnumber + secondnumber
elif options == 2:
    print(f"What is {firstnumber} - {secondnumber}?")
    result = firstnumber - secondnumber
elif options == 3:
    print(f"What is {firstnumber} * {secondnumber}?")
    result = firstnumber * secondnumber
elif options == 4:
    print(f"What is {firstnumber} / {secondnumber}?")
    result = firstnumber / secondnumber
#user solution
usersolution = int(input('input solution: '))
if usersolution == result :
    print ('Correct')
else:
    print ('Incorrect')
    print("Correct answer:", result)