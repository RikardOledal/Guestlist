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