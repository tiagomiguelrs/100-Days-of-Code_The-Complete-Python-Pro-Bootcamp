print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Children tickets are $5.")
        bill += 5
    elif age <= 18:
        print("Teens tickets are $7.")
        bill += 7
    else:
        print("Adult tickets are $12.")
        bill += 12

    photo = input("Do you want photo?: ")
    if photo == "yes":
        print("Photo will be extra 3 $")
        bill += 3

    print(f"The bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
