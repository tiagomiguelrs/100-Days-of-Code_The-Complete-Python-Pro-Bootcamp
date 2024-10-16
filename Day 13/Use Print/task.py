word_per_page = 0
pages = int(input("Number of pages: "))

# This equality gives False disguised as 0 because 0 is not equal to any other number.
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))

print(f"Words per page are {word_per_page}")
total_words = pages * word_per_page
print(f"Total words are {total_words}")
