# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Do you live by {location}?")


greet_with_name("Jack Bauer", "Nova Gaia")


# Keyword arguments (kwargs) should always come after the remaining arguments (args)
# Otherwise an error will be raised
def greet_again(name="Jack Bauer", location="Nova Gaia"):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Do you live by {location}?")


greet_with_name(location="Netherlands", name="Jean Pierre")
