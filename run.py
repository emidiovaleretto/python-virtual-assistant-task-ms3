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


def print_menu():
    """
    Prints the menu of options.
    """
    chatboot_message(
        "\n[1] Add a new task\n[2] View all tasks\n[3] Delete a task\n[4] Restore a deleted task\n[5] Exit"
    )


def add_new_task():
    """
    Adds a new task to the list.
    """
    chatboot_message("\nWhat task would you like to add?\n")
    task = input("\n>> ")
    task_list.append(task)
    chatboot_message(f"\nGreat! Let's add [{task.upper()}] to your list.\n")
    chatboot_message("Adding task...")
    sleep(1)
    chatboot_message(f"\nTask added!\n")


def ask_to_add_task():
    """
    Asks the user if he/she wants to add a new task.
    """
    chatboot_message("\nWould you like to add a new task? [y/N]")
    answer = input("\n>> ")[0].strip().lower()

    if answer == "y":
        add_new_task()

    else:
        chatboot_message(
            "\nThank you so much for using our chat service. "
            "\nWe hope we will hear from you soon! \nHave a good day.\n"
        )
        sleep(1)
        sys.exit()


def view_all_tasks():
    """
    Prints a list of tasks.
    """
    if not task_list:
        sleep(1)
        chatboot_message("\nYour list is still empty.\n")
        ask_to_add_task()

    else:
        chatboot_message(f"\nHere is your list of tasks:\n")

        for i, task in enumerate(task_list):
            i += 1
            print(f"\n\t{i} - {task}")
            sleep(0.05)


def view_removed_tasks():
    """
    Returns a list of removed tasks.
    """
    return removed_items


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
        view_all_tasks()
        task_to_delete = int(input("\n>> "))

        for i, task in enumerate(task_list):
            if task_to_delete == i + 1:
                removed_task = task_list.pop(i)
                removed_items.append(removed_task)
                sleep(1)
                return chatboot_message(f"\nTask [{task}] removed!\n")


def main():
    """
    Run all program functions.
    """
    greetings()
    username = input("\n>> ")
    chatboot_message(
        f"Hi, {username}. Thank you for using our chat service. \nHow may I assist you today?\n"
    )

    while True:
        print_menu()
        user_choice = input("\n>> ")

        if not user_choice.isdigit():
            chatboot_message("\nPlease enter a valid option.\n")
        else:
            user_choice = int(user_choice)

            if user_choice == 1:
                add_new_task()

            elif user_choice == 2:
                view_all_tasks()

            elif user_choice == 3:
                remove_task()

            else:
                chatboot_message("\nOption not available yet.\n")
                break


removed_items = []
task_list = []

main()
