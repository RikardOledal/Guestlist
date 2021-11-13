options = input("input opperator: ")
firstnumber = int(input("input first number: "))
secondnumber = int(input("input second number: "))
if options == "+" :
    result = firstnumber + secondnumber
    print("answer:", result)
elif options == "-":
    result = firstnumber - secondnumber
    print("answer:", result)
elif options == "*":
    result = firstnumber * secondnumber
    print("answer:", result)
elif options == "/":
    result = firstnumber / secondnumber
    print("answer:", result)