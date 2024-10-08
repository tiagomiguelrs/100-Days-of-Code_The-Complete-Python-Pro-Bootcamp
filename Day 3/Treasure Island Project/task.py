print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are standing at the shore line of a tropical island where pirates have buried "
      "many treasures through the ages.")
print("You enter the thick vegetation in search for one such treasure.")
print("You hear a sound from behind.")
print("You look back and find a flock of angry dodos that want you out of their real estate!")
print("You start running before they get to you!!")

tries = 3
win = False
direction = None
action = None
door = None

direction = input("An intersection is just up ahead. Run left or right.").lower()
while tries > 0:

    if action is None and door is None:
        if direction == "right":
            print("You find yourself running in circles until you go back to the same intersection. "
                  "The dodos are getting closer! Try again.")
            tries -= 1
            if tries <= 0:
                print("The angry dodos got to you!")
                break
            else:
                direction = input("An intersection is just up ahead. Run left or right.").lower()
        elif direction == "left":
            action = input("You find a big pond and a small semi torn raft. You look beyond the pond and see "
                           "an entrance. Do you try sailing the raft or will you swim across? ").lower()
        else:
            print("Your were indecisive. The angry dodos got to you and they pounded your ass to death.")
            break

    if direction == "left" and door is None:
        if action == "swim" or action == "swimming":
            print("A crocodile approached you holding a fork and a knife. You try to run away.")
            tries -= 1
            if tries <= 0:
                print("You are dead toast")
                break
            else:
                print("You run back to land, but the angry dodos are ever closer!")
        elif action == "sail" or action == "sailing":
            action = "sail"
            print("You escaped any harm and find the safety of lnd on the other side of the pond.")
        else:
            print("Your were indecisive. The angry dodos got to you and they pounded your ass to death.")
            break

    if action == "sail" and direction == "left":
        door = input("There are three doors to the entrance of the cave. Red door, yellow door and blue door. "
                     "Which are you going to choose? ").lower()
        if door == "red":
            print("You open a door to an immense fire!")
            tries -= 1
            if tries <= 0:
                print("Fire engulfs you. You are burnt toast.")
                break
            else:
                print("You quickly close the door before you get burnt.")
        elif door == "blue":
            print("You see an unknown beast with three heads, and huge teeth!")
            tries -= 1
            if tries <= 0:
                print("The beast got you. You are chewed to death.")
                break
            else:
                print("You quickly close the door before the beast bites you.")
        elif door == "yellow":
            win = True
            print("You find a sea of golden coins!")
            break
        else:
            print("Your were indecisive. The angry dodos got to you and they pounded your ass to death.")
            break

if win:
    print("Congrats you got the treasure and escaped the angry dodos!")
else:
    print("Game over.")