def add(n1, n2):
    return n1 + n2


# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

# We are storing and not using the functions, so we don't use "()"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

# print(operations["*"](4, 8))

# ---------------------------------------------------------------------------------------------
from art import logo

def calculator():
    print(logo)

    n1 = float(input("Please type the first number:\n"))

    keep_calculating = True
    while keep_calculating:

        operation = input("Please choose the desired operation typing:\n"
                          "+ for addition\n"
                          "- for subtraction\n"
                          "* for multiplication\n"
                          "/ for division\n")
        n2 = float(input("Please type the second number:\n"))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}.")
        keep_going = input("Do you want to keep going? Type [y] for yes or [n] for no.\n")
        if keep_going == "y":
            n1 = result
        elif keep_going == "n":
            print("\n" * 20)
            keep_calculating = False
            calculator()    # Neat use of recursion
        else:
            print("Invalid input, we keep going!")
            n1 = result


calculator()
