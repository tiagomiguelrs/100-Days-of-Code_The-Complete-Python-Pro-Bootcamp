import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# placeholder = "".join(["_" for letter in chosen_word])
# OR
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

guess = input("Guess a letter: ").lower()[0]

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# display = []
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         display.append(guess)
#         print("Right")
#     else:
#         display.append("_")
#         print("Wrong")
#
# print("".join([letter for letter in display]))

# OR

display = ""
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display += guess
        print("Right")
    else:
        display += "_"
        print("Wrong")

print(display)