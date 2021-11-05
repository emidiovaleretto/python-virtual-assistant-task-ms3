import os
import sys
from random import choice
from time import sleep
from send_email import send_email


def typing_effect(text):
    """
    Prints text with a typing effect.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)


def chatbot_message(text):
    """
    Returns the chatbot message.
    """
    return typing_effect(log(text, "Agent"))


def choose_name_randomly():
    """
    Returns a random name from an external file called names.txt.
    """
    with open("names.txt", "r") as name_list:
        name = [name for name in name_list.read().splitlines()]
        return choice(name)


def greetings():
    """
    Prints a greeting to the user.
    """
    chosen_name = choose_name_randomly()
    chatbot_message(
        f"Hello, my name is {chosen_name}. It's nice to speak with you."
        "\nMay I please have your name?"
    )


def print_menu():
    """
    Prints the menu of options.
    """
    chatbot_message(
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

    return log(int(user_input), "User")


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
        chatbot_message(f"{err}")
        return False

    return True


def start_bot():
    """
    Starts bot.
    Run a while loop to get the user choice.
    The loop will continue to prompt the user until
    he/she decides to exit the program.
    """
    while True:

        user_choice = get_user_input()

        if user_choice == 1:
            add_new_task()

        elif user_choice == 2:
            chatbot_message("\nHere is your list of tasks:\n")
            view_all_tasks(task_list)

        elif user_choice == 3:
            remove_task()

        elif user_choice == 4:
            restore_task()

        elif user_choice == 5:
            end_chat()

        else:
            chatbot_message("\nPlease enter a valid option.\n")


def add_new_task():
    """
    Adds a new task to the list.
    """
    chatbot_message("\nWhat task would you like to add?\n")
    task = input("\n>> ").strip()

    chatbot_message(f"\nGreat! Let's add [{task.upper()}] to your list.\n")
    chatbot_message("Adding task...")

    task_list.append(task.capitalize())
    sleep(1)

    chatbot_message(f"\nTask added!\n")
    ask_to_add_task()


def view_all_tasks(list):
    """
    Prints a list of tasks.
    """
    if not list:
        sleep(1)
        chatbot_message("\nYour list is still empty.\n")
        ask_to_add_task()

    else:
        for i, task in enumerate(list):
            i += 1
            print(f"\n{i} - {task}")

        sleep(1)


def remove_task():
    """
    Returns a removed task from the list.
    """
    if not task_list:
        sleep(1)
        chatbot_message("\nThere is no tasks to be removed.\n")
        ask_to_add_task()

    else:
        chatbot_message(f"\nWhich task would you like to delete?\n")
        view_all_tasks(task_list)
        task_to_delete = get_user_input()

        for i, task in enumerate(task_list):
            if task_to_delete == i + 1:
                removed_task = task_list.pop(i)
                removed_items.append(removed_task)
                sleep(1)
                return chatbot_message(f"\nTask [{task}] removed!\n")


def restore_task():
    """
    Restores a removed task.
    """
    if not removed_items:
        sleep(1)
        chatbot_message("\nThere is no tasks to be restored.\n")
        ask_to_add_task()

    else:
        chatbot_message(f"\nWhich task would you like to restore?\n")
        view_all_tasks(removed_items)
        task_to_restore = get_user_input()

        for i, task in enumerate(removed_items):
            if task_to_restore == i + 1:
                restored_task = removed_items.pop(i)
                task_list.append(restored_task)
                sleep(1)
                return chatbot_message(f"\nTask [{task}] restored!\n")


def end_chat():
    """
    Prints a message to the user ending the conversation.
    """
    chatbot_message(
        "\nI'm glad I was able to get that sorted out for you. "
        "\nBefore you go, would you like to get a copy of this chat? [y/N]"
    )

    answer = input("\n>> ")[0].strip().lower()

    if answer == "y":
        chatbot_message("\nGreat! Enter your email address below:")
        email = input("\n>> ").strip()
        send_email(email, "Here is your conversation log.")
        print("\nSending email...")
        sleep(5)
        chatbot_message(
            "\nOK, all done! Check your inbox for an email "
            "with the LiveChat transcript.\n"
        )

    chatbot_message(
        "\nThank you so much for using our chat service. "
        "\nWe hope we will hear from you soon. \nHave a great day!\n"
    )
    sleep(1)
    os.remove("log.txt")
    sys.exit()


def ask_to_add_task():
    """
    Asks the user if he/she wants to add a new task.
    """
    chatbot_message("\nWould you like to add a new task? [y/N]")
    answer = input("\n>> ")[0].strip().lower()

    if answer == "y":
        add_new_task()

    else:
        chatbot_message("\nOkay, let me show you some other options.\n")
        # then loop goes back to the main thread (print_menu)


def log(message, person):
    """
    Logs the conversation and save to an external file.
    """
    path = "log.txt"

    with open(path, "a", newline="") as log_file:
        log_file.write(f"[{person}] - {message}\n")
        return message


def main():
    """
    Run all program functions.
    """
    greetings()
    username = input("\n>> ").strip().capitalize()
    chatbot_message(
        f"\nHi, {username}. Thank you for using our chat service. "
        "\nHow may I assist you today?\n"
    )
    start_bot()


removed_items = []
task_list = []
