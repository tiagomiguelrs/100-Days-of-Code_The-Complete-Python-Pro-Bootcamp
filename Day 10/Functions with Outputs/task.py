def format_name(f_name, l_name):
    return f_name.title(), l_name.title()

first = input("Write you first name.\n")
last = input("Write your last name.\n")

first_titled, last_titled = format_name(first, last)
print(first_titled, last_titled)

# -----------------------------------------------------------------------------------------
# "Nested" functions

def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)
