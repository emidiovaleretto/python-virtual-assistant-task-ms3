from random import choice


def choose_name_randomly():
    """
    Returns a random name from a list of names.
    """
    list_names = [
        'John', 'Paul', 'George', 'Ringo', 'Sam', 'Ciara', 'Fiona', 'Jessica',
        'Natalie', 'Emma'
    ]
    return choice(list_names)


def greetings(name):
    """
    Returns a greeting to user.
    """
    return f"Hello, this is {name}. It's nice to speak with you." \
             "\nMay I please have your name?"


def main():
    """
    Run all program functions.
    """
    chosen_name = choose_name_randomly()
    print(greetings(chosen_name))


main()