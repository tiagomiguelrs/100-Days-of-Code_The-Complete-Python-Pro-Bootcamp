def format_name(f_name, l_name):
    """
    Take the first and last name and format it
    to return the title case version of the input variables.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
