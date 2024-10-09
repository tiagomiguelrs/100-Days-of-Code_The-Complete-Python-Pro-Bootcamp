import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

letters_in_password = []
numbers_in_password = []
symbols_in_password = []

for l in range(nr_letters):
    i = random.randint(0, len(letters)-1)
    letters_in_password.append(letters[i])
    letters.pop(i)

for n in range(nr_numbers):
    i = random.randint(0, len(numbers)-1)
    numbers_in_password.append(numbers[i])
    numbers.pop(i)

for s in range(nr_symbols):
    i = random.randint(0, len(symbols)-1)
    symbols_in_password.append(symbols[i])
    symbols.pop(i)

print(letters_in_password, numbers_in_password, symbols_in_password)

characters = []
characters.extend(letters_in_password)
characters.extend(numbers_in_password)
characters.extend(symbols_in_password)
random.shuffle(characters)

password = "".join(characters)
print(password)