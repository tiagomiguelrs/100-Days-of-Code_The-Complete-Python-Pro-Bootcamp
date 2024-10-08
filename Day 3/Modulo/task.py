number = int(input("Please choose a number: "))

rem = number % 2

if rem == 0:
    print(f"the number {number} is even, and the remainder is {rem}")
else:   # Remainder == 1
    print(f"The number {number} is odd, and the remainder is {rem}")
