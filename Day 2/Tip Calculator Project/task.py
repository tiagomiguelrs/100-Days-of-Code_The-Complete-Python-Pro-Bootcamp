print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


pay = (bill / people) * (1 + tip / 100)
print(f"Each person should pay {round(pay, 2):.2f}$")
# If I only use round(pay, 2) I will only get 33.6 because the next number is 0
# and it is not shown