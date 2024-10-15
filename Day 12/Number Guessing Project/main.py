from art import logo
from random import randint

EASY_DIFFICULTY_TRIES = 5
HARD_DIFFICULTY_TRIES = 10

# TODO-1 Create a function that generates a number to guess
def generate_number():
    return randint(1, 100)


# TODO-2 Create a function that verifies if the guessed number is correct
def is_correct(guess):
    if guess == GUESS_NUMBER:
        print(f"That's correct! The number was {GUESS_NUMBER}.")
        return True
    else:
        print(f"{guess} is not the correct number.")
        return False


# TODO-3 Create a function that tells if the number is too high or too low
def high_or_low(guess):
    if guess < GUESS_NUMBER:
        print(f"The number {guess} is too low.")
    else:
        print(f"The number {guess} is too high.")


# TODO-4 Create a function that sets the number of tries for easy and hard level
def number_of_tries(dif):
    if dif == "hard":
        return EASY_DIFFICULTY_TRIES
    else:
        return HARD_DIFFICULTY_TRIES


# TODO-6 Encase the loop in a function
def guess_the_number():
    # TODO-5 Generate the guessing loop
    tries = number_of_tries(input("Please choose difficulty 'hard' for 5 tries or 'easy' for 10 tries.\n"))
    guessed = False
    while tries > 0 and not guessed:
        guess_number = int(input("Guess a number between 1 and 100:\n"))
        if is_correct(guess_number):
            guessed = True
        else:
            tries -= 1
            print(f"You have {tries} tries.")
            high_or_low(guess_number)

        if tries == 0:
            print(f"The guessing number was {GUESS_NUMBER}")


GUESS_NUMBER = generate_number()
print(logo)
guess_the_number()
