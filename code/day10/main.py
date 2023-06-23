# day 10 - Functions

# def my_function(something):
# do something

# Functions with Outputs
def my_function():
    return 3 * 2


def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case of the name"""
    if f_name == "" or l_name == "":
        return
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


format_name("aMEeN", "DE SILVA")
print(format_name(input("What is your first name? \n"), input("What is your last name? \n")))

#Docstrings
#adds the first multiline comment in the first indented line under a function like line 12

