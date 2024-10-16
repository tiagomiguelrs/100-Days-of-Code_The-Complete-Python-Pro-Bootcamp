def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# The function contains a loop that uses a range to advance iterations.
# At iteration == 20, the function should print "You got it".

# 1. What is the for loop doing?
# The for loop iterates between 1 including and 20 excluding.

# 2. When is the function meant to print "You got it"?
# The function is meant to print "You got it" at iteration 20 including

# 3. What are your assumptions about the value of i?
# The value of 1 will never be 20 so the function will never print the wanted string.
