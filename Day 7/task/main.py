import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

game_over = False
guesses = []
lives = 6
while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    guesses.append(guess)
    print(guesses)
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter in guesses:   # Checks if the correct letter is in the user's guesses
            for g in guesses:
                if letter == g: # If so, it will check which of the guesses fit in that place
                    display += letter
        else: display += "_"    # Else it will place a placeholder

    print(display)
    
    if guesses[-1] not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lost!")
            game_over = True
    
    if "_" not in display:
        print("You won!")
        game_over = True

