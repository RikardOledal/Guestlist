# Task 4 - The Math quiz
import random
print("Lets see your math-skilz!!!")
print("(Print quit if you give up)")

points = 0
while points < 10:
    # Randomchoice of function
    sign = random.randint(1, 4)
    # 1 == +
    # 2 == -
    # 3 == *
    # 4 == /
    # Depending on number you get different functions
    firstnumber = random.randint(1, 9)
    secondnumber = random.randint(1, 9)
    if points == 5:
        print("You are good!!!")
    if sign == 1:
        answer = input(f"What is {firstnumber} + {secondnumber}")
        if answer == "quit":
            break
        elif int(answer) == firstnumber + secondnumber:
            print("That is correct! 1 point for you")
            points += 1
            print(f"You now have {points} points")
        else:
            print(f"WRONG!!! The right answer is {firstnumber+secondnumber}")
    elif sign == 2:
        answer = input(f"What is {firstnumber} - {secondnumber}")
        if answer == "quit":
            break
        elif int(answer) == firstnumber - secondnumber:
            print("That is correct! 1 point for you")
            points += 1
            print(f"You now have {points} points")
        else:
            print(f"WRONG!!! The right answer is {firstnumber-secondnumber}")
    elif sign == 3:
        answer = input(f"What is {firstnumber} * {secondnumber}")
        if answer == "quit":
            break
        elif int(answer) == firstnumber * secondnumber:
            print("That is correct! 1 point for you")
            points += 1
            print(f"You now have {points} points")
        else:
            print(f"WRONG!!! The right answer is {firstnumber*secondnumber}") 
    elif sign == 4:
        answer = input(f"What is {firstnumber} / {secondnumber}")
        if answer == "quit":
            break
        elif float(answer) == firstnumber / secondnumber:
            print("That is correct! 1 point for you")
            points += 1
            print(f"You now have {points} points")
        else:
            print(f"WRONG!!! The right answer is {firstnumber/secondnumber}")
print("I've have had enoght!!! You win!!!")