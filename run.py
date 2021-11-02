import sys
from random import choice
from time import sleep


def typing_effect(text):
    """
    Prints text with a typing effect.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.03)


def choose_name_randomly():
    """
    Returns a random name from a list of names.
    """
    list_names = [
        "John",
        "Paul",
        "George",
        "Ringo",
        "Sam",
        "Ciara",
        "Fiona",
        "Jessica",
        "Natalie",
        "Emma",
    ]
    return choice(list_names)


def greetings(name):
    """
    Prints a greeting to the user.
    """
    typing_effect(
        f"Hello, my name is {name}. It's nice to speak with you."
        "\nMay I please have your name?"
    )


def print_menu():
    """
    Prints the menu of options.
    """
    typing_effect(
        "\n[1] Add a new task\n[2] View all tasks\n[3] Delete a task\n[4] Exit\n"
    )


def main():
    """
    Run all program functions.
    """
    chosen_name = choose_name_randomly()
    greetings(chosen_name)
    username = input("\n>> ")

    typing_effect(f"\nRight, {username}! How may I assist you today?\n")

    print_menu()

    user_choice = input("\n>> ")

    typing_effect(
        f"\Okay, {username}, your choice was: {user_choice}. let's get started!\n"
    )


main()
