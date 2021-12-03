stock = {"Appel":5, "Lemon":5, "Orange":5}
prices = {}
sales = {}
store = {}

print(stock)

x = 3
stock.update({"Appel":stock["Appel"]+x})
print(stock)
stock.update({"Pineappel":x})
print(stock)

test = 30
procent = 10
Newprice = test*(1-(procent/100))
print(Newprice)
