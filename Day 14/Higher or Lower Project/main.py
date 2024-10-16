# TODO-1 Make necessary imports
from imagecodecs import NoneError

from art import logo, vs
from game_data import data
from random import randint

CELEBRITY_DATA = data

# TODO-2 Create a function that randomly chooses a celebrity
def choose_celebrity():
    return CELEBRITY_DATA[randint(0, len(CELEBRITY_DATA)-1)]


# TODO-3 Verify that the celebrities are not the same
# Unused because of a while loop in the higher_lower() function
def are_different(celeb1, celeb2):
    """
    Verifies that the celebrities are different.
    celeb1 and celeb2 are two dictionaries extracted from the main list.
    """
    if celeb1["name"] == celeb2["name"]:
        return False
    else:
        return True


# TODO-6 Create a function that compares the number of followers
def compare_followers(celeb1, celeb2):
    print(celeb1["follower_count"])
    print(celeb2["follower_count"])
    if celeb1["follower_count"] >= celeb2["follower_count"]:
        return True
    elif celeb1["follower_count"] < celeb2["follower_count"]:
        return False


def player_choice(c):
    if c == "A":
        return True
    elif c == "B":
        return False
    else:
        raise NoneError


# # TODO-11 Create a try-except function that validates that the answer given is in the correct form
def validate_answer(c):
    try:
        answer = player_choice(c)
        return answer
    except NoneError:     # In case the player types a letter other than A or B
        c = input("Invalid answer. Please type 'A' or 'B': ")
        validate_answer(c)


# TODO-9 Turn the Higher Lower loop into a function and call it bellow
def higher_lower(celeb1, celeb2):
    score = 0

    # TODO-7 Create a while loop that loops while the answer is correct
    correct = True
    while correct:

        # TODO-5 Create a while loop to choose a second celebrity that is never equal to the first celebrity
        while celeb2 == celeb1 or celeb2 == {}:
            celeb2 = choose_celebrity()

        is_A_greater = compare_followers(celeb1, celeb2)

        print("\n" * 20)
        print(logo)
        print(f"Your score is {score}")

        print(f"Compare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")

        print(vs)

        print(f"Against B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}")

        choice = input("Who has more followers? Type A or B. ").upper()
        answer_bool = validate_answer(choice)
        print(answer_bool)
        if is_A_greater == answer_bool:
            print("That's correct!")
            score += 1

            # TODO-8 Turn celeb2 into celeb1
            celeb1 = celeb2

        else:
            print("You missed!")
            print(f"Your final score was {score}")
            correct = False


# TODO-4 Choose starting celebrity
celebrity1 = choose_celebrity()
celebrity2 = {}

# TODO-10 Create a loop that keeps playing
keep_playing = True
while keep_playing:
    higher_lower(celebrity1, celebrity2)

    restart = input("Do you want to play again? Type [y] for yes or [n] for no.\n")
    if restart == "y":
        print("Let's go!")
    else:
        print("Ok, bye!")
        keep_playing = False