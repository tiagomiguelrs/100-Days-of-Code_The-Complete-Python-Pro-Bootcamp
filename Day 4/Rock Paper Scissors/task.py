rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# --------------------------------------------------------------------------------

import random

hand = [rock, paper, scissors]
print(hand[0])

while True:
    player = input("Choose rock, paper or scissors:\n").lower()
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.\n")
    else:
        if player == "rock":
            player_choice = 0
        elif player == "paper":
            player_choice = 1
        elif player == "scissors":
            player_choice = 2
        break

player_hand = hand[player_choice]    # If while loop is stopped without a choice it will raise problems

computer_choice = random.randint(0, len(hand)-1)
computer_hand = hand[computer_choice]

print("Your choice:\n")
print(player_hand + "\n\n")

print("Computer choice:\n")
print(computer_hand + "\n\n")

if player_choice == 0:
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")

elif player_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("It's a draw")
    elif computer_choice == 2:
        print("You lose")

else:   # No use using an elif for safety because choices are locked in the while loop
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    elif computer_choice == 2:
        print("It's a draw")
