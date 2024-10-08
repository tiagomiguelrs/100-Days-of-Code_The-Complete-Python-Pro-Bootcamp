print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
wrong_flag = False
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
else:
    print("You printed the wrong inputs.")
    wrong_flag = True

if not wrong_flag and extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
