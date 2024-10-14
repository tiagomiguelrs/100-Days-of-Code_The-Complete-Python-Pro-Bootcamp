def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return  "You did not provide valid inputs" # Ends the function earlier
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("First name: "), input("Last name: ")))

# Return ends the function. Nothing after gets executed
