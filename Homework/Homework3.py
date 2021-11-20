# Task 1: String manipulation

word = "Rikard Oledal"

if len(word) < 2:
    print("Empty String")
else:
    print(word[0:2]+word[len(word)-2:len(word)])

# Task 2: Phonenumber-check

phone = "0738394420"
i = 0
roof = len(phone)-1

# Check length
if len(phone) != 10:
    print("Your number phonenumber must be 10 digits")
# Check digits
while i <= roof:
    if not phone[i].isdigit():
        print(f"The {i+1} character is not a digit")
    i += 1
    continue
# Check digits and length
if phone.isdigit and len(phone) == 10:
    print("It is a correct phonenumber with 10 digits")
else:
    print("Correct the errors above!")

# Task 3: Name-check

my_name = "rikard"
print("Guess what name I am thinking of")
guess = input()
if guess.isupper:
    guess = guess.lower()
if guess == my_name:
    print("Congratulations!!! You guessed right")
else:
    print("You are wrong!!!")