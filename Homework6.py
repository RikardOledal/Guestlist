# Task 1 - Wordcounter

# display intro
title = " ** Word Counter ** "
print ("\n")
print ("*" * len(title))
print (title)
print ("*" * len(title))
print ("\n")

# Userintegration
sentence = input("Please provide me with a text:").lower()

# Remove unwanted signs
specialchar = ["!", "?", "%", ",", "&", "/", "(", ")", "."]
for sign in specialchar:
    sentence = sentence.replace(sign, "")

# Create dict to summurize how many of eche word it is
words = dict()
for parts in sentence.split():
    if parts in words:
        words[parts] += 1
    else:
        words[parts] = 1

# Print the result
print("Your words are:")
print(words)

# Task 2 - Fruitmarket

# display intro
title = " ** Fruitmarket ** "
print ("\n")
print ("*" * len(title))
print (title)
print ("*" * len(title))
print ("\n")

# pre-set values
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Calculations for totalcost
totalcost = 0
for fruit in stock:
    if fruit in prices:
        totalcost += stock[fruit]*prices[fruit]

totalcost = int(totalcost)
print(f"The total value of the fruit is {totalcost}")

# Task 3 - Squared tuplets-list

# display intro
title = " ** Squared tuplets-list ** "
print ("\n")
print ("*" * len(title))
print (title)
print ("*" * len(title))
print ("\n")

# List from 1-10
numbers = list(range(1,11))

# Comprehension for geting the squared tuplets-list
squared_tup = [(i, i*i) for i in numbers]

# Printing the result
print(squared_tup)