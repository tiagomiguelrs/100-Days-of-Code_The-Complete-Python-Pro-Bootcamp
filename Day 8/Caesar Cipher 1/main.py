from math import ceil

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    shifted_text = ""
    for l in original_text.lower():
        if l != " ":
            original_index = alphabet.index(l)
            shifted_index = original_index + shift_amount
            # If new letter index is greater than list length, restart index
            if shifted_index >= len(alphabet):
                rotations = ceil(shifted_index//len(alphabet))
                max_length = len(alphabet)
                shifted_index -= int(max_length * rotations)
            shifted_text += alphabet[shifted_index]
        else:
            shifted_text += " "

    print(shifted_text)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)
