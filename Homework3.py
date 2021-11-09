# Task 1: String manipulation

word = "Rikard Oledal"

if len(word) < 2:
    print("Empty String")
else:
    print(word[0:2]+word[len(word)-2:len(word)])

# Task 2: Phonenumber-check

phone = "085694A22"
i = 0
roof = 10

# Check that the length of the number is 10 digits
if len(phone) != 10:
    print("Your number phonenumber must be 10 digits")
else:
    print("Your number is the correct length")
# Check if any numbers are not digits
while i <= 10:
    if not phone[i].isdigit():
        print(f"The {i-1} character is not a digit")
        i += 1
        continue
if phone.isdigit and len(phone) == 10:
    print("It is a correct phonenumber with 10 numbers")
else:
    print("Correct the Errors above!")

