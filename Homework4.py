# Task 1 - The Guessing Game.
import random

print("\n")
print("The Guessing Game")
print("\n")

print("Let's play a game! I'm thinking of a number between 1-10.")
guess = input("What number am I thinking of?")

if guess == "1" or guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6" or guess == "7" or guess == "8" or guess == "9" or guess == "10":
    computer = random.randint(1, 10)
    # 1 == 1
    # 2 == 2
    # 3 == 3
    # 4 == 4
    # 5 == 5
    # 6 == 6
    # 7 == 7
    # 8 == 8
    # 9 == 9
    # 10 == 10
    if (str(computer) == guess):
        print(f"Congratulations I was also thinking of {guess}. You win!")
    else:
        print(f"WRONG!!! I was thinking of {computer}")

# Task 2 - The birthday greeting program.

print("\n")
print("The birthday greeting program")
print("\n")

name = input("Hello! My name is Arthur. What is your name?")
if not name.isalpha():
    print("Your name does not include numbers. If you aint taking this serious I'm not going to speak to you!")
else:
    age =input(f"{name}. What a beautiful name! How old are you?")
    if not age.isdigit():
        print(f"Come on! {age.title()} is not a number!")
    else:
        print(f"WOW! That means that you {name} will be {int(age)+1} next year!")

# Task 3 - Words combination.

print("I can scramble words. Try me!")
word = input("Give me a word!")
if not word.isalpha():
    print("Just letters. No numbers.")
else:
    print(f"Let's scramble the word {word}!!!")
    i = 1
    while i <= 5:
        result = random.sample(word, k=len(word))
        print("".join(result))
        i += 1

# Task 4 - The Math quiz
print("Lets see your math-skilz!!!")
# Randomchoice of function
sign = random.randint(1, 4)
    # 1 == +
    # 2 == -
    # 3 == *
    # 4 == /
firstnumber = random.randint(1, 9)
secondnumber = random.randint(1, 9)
# Depending on number you get different functions
if sign == 1:
    answer = input(f"What is {firstnumber} + {secondnumber}")
    if int(answer) == firstnumber + secondnumber:
        print("That is correct! You are a genius!!!")
    else:
        print(f"WRONG!!! The right answer is {firstnumber+secondnumber}")
elif sign == 2:
    answer = input(f"What is {firstnumber} - {secondnumber}")
    if int(answer) == firstnumber - secondnumber:
        print("That is correct! You are a genius!!!")
    else:
        print(f"WRONG!!! The right answer is {firstnumber-secondnumber}")
elif sign == 3:
    answer = input(f"What is {firstnumber} * {secondnumber}")
    if int(answer) == firstnumber * secondnumber:
        print("That is correct! You are a genius!!!")
    else:
        print(f"WRONG!!! The right answer is {firstnumber*secondnumber}")
else:
    answer = input(f"What is {firstnumber} / {secondnumber}")
    if float(answer) == firstnumber / secondnumber:
        print("That is correct! You are a genius!!!")
    else:
        print(f"WRONG!!! The right answer is {firstnumber/secondnumber}")