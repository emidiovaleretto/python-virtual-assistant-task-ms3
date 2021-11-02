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


chosen_name = choose_name_randomly()
print(f'Hello, {chosen_name}!')