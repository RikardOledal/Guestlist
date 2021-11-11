# Python Application
import random
print("Lets see your math-skilz!!!")
sign = random.randint(1, 4)
    # 1 == +
    # 2 == -
    # 3 == *
    # 4 == /
firstnumber = random.randint(1, 9)
secondnumber = random.randint(1, 9)
answer = input(f"What is {firstnumber} / {secondnumber}")
if float(answer) == firstnumber / secondnumber:
    print("That is correct! You are a genius!!!")
else:
    print(f"WRONG!!! The right answer is {firstnumber/secondnumber}")