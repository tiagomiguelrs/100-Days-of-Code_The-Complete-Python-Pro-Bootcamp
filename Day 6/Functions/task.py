def my_function():
    print("Hello")
    print("Bye")

my_function()

#-----------------------------------------------------------------------------
# Reeborg's world solution to maze problem (https://reeborg.ca/)

def turn_right():   # Instead of writing turn_left() three times every time we need to go right. Make a function.
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():    # Avoids the occurence of a specific situation where reeborg does not have a wall from which to guide itself in the beginning.
    move()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()