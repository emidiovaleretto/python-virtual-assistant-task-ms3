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
        sleep(0.02)


def chatboot_message(text):
    """
    Returns the chatboot message.
    """
    return typing_effect(text)


def choose_name_randomly():
    """
    Returns a random name from a list of names.
    """
    list_names = [
        "John",
        "Paul",
        "George",
        "Ben",
        "Sam",
        "Ciara",
        "Fiona",
        "Jessica",
        "Natalie",
        "Emma",
    ]
    return choice(list_names)


def greetings():
    """
    Prints a greeting to the user.
    """
    chosen_name = choose_name_randomly()
    chatboot_message(
        f"Hello, my name is {chosen_name}. It's nice to speak with you."
        "\nMay I please have your name?"
    )


def get_username():
    """
    Returns the user name input.
    """
    return input("\n>> ")


def print_menu():
    """
    Prints the menu of options.
    """
    chatboot_message(
        "\n[1] Add a new task"
        "\n[2] View all tasks"
        "\n[3] Delete a task"
        "\n[4] Restore a task"
        "\n[5] Exit"
    )


def get_user_input():
    """
    Returns the user input.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be a digit.
    The loop will continue to prompt the user until the data is valid.
    """

    while True:

        print_menu()
        user_input = input("\n>> ")
        is_valid_input = validate_input(user_input)

        if is_valid_input:
            break

    return int(user_input)


def validate_input(user_input):
    """
    Validates the user input.
    Inside the try/except block, the user is prompted
    to enter the data type. Raises a ValueError if
    data type is not a digit.
    """

    try:
        if user_input.isdigit():
            int(user_input)
        else:
            raise ValueError(f"\n'{user_input}' is not a valid data type.\n")

    except ValueError as err:
        chatboot_message(f"{err}")
        return False

    return True


def add_new_task():
    """
    Adds a new task to the list.
    """
    chatboot_message("\nWhat task would you like to add?\n")
    task = input("\n>> ").strip()
    task_list.append(task.capitalize())
    chatboot_message(f"\nGreat! Let's add [{task.upper()}] to your list.\n")
    chatboot_message("Adding task...")
    sleep(1)
    chatboot_message(f"\nTask added!\n")


def view_all_tasks(list):
    """
    Prints a list of tasks.
    """
    if not list:
        sleep(1)
        chatboot_message("\nYour list is still empty.\n")
        ask_to_add_task()

    else:
        for i, task in enumerate(list):
            i += 1
            print(f"\n{i} - {task}")
            sleep(0.05)


def remove_task():
    """
    Returns a removed task from the list.
    """
    if not task_list:
        sleep(1)
        chatboot_message("\nThere is no tasks to be removed.\n")
        ask_to_add_task()

    else:
        chatboot_message(f"\nWhich task would you like to delete?\n")
        view_all_tasks(task_list)
        task_to_delete = int(input("\n>> "))

        for i, task in enumerate(task_list):
            if task_to_delete == i + 1:
                removed_task = task_list.pop(i)
                removed_items.append(removed_task)
                sleep(1)
                return chatboot_message(f"\nTask [{task}] removed!\n")


def restore_task():
    """
    Restores a removed task.
    """
    if not removed_items:
        sleep(1)
        chatboot_message("\nThere is no tasks to be restored.\n")

    else:
        chatboot_message(f"\nWhich task would you like to restore?\n")
        view_all_tasks(removed_items)
        task_to_restore = int(input("\n>> "))

        for i, task in enumerate(removed_items):
            if task_to_restore == i + 1:
                restored_task = removed_items.pop(i)
                task_list.append(restored_task)
                sleep(1)
                return chatboot_message(f"\nTask [{task}] restored!\n")


def end_chat():
    """
    Prints a message to the user ending the conversation.
    """
    chatboot_message(
        "\nI’m glad I was able to get that sorted out for you. "
        "\nBefore you go, is there anything else I can assist "
        "you with today? [y/N]"
    )

    answer = input("\n>> ")[0].strip().lower()

    if answer == "y":
        chatboot_message(
            "\nNot problem at all. \nI'm going to show you some options.\n"
        )

    else:
        chatboot_message(
            "\nThank you so much for using our chat service. "
            "\nWe hope we will hear from you soon. \nHave a great day!\n"
        )
        sleep(1)
        sys.exit()


def ask_to_add_task():
    """
    Asks the user if he/she wants to add a new task.
    """
    chatboot_message("\nWould you like to add a new task? [y/N]")
    answer = input("\n>> ")[0].strip().lower()

    if answer == "y":
        add_new_task()

    else:
        end_chat()


def view_removed_tasks():
    """
    Returns a list of removed tasks.
    """
    return removed_items


def main():
    """
    Run all program functions.
    """
    greetings()
    username = get_username()
    chatboot_message(
        f"\nHi, {username}. Thank you for using our chat service. "
        "\nHow may I assist you today?\n"
    )

    while True:

        user_choice = get_user_input()

        if user_choice == 1:
            add_new_task()

        elif user_choice == 2:
            chatboot_message("\nHere is your list of tasks:\n")
            view_all_tasks(task_list)

        elif user_choice == 3:
            remove_task()

        elif user_choice == 4:
            restore_task()

        elif user_choice == 5:
            end_chat()

        else:
            chatboot_message("\nPlease enter a valid option.\n")


removed_items = []
task_list = []

main()
