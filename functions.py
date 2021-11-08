import sys
import os
from random import choice
from time import sleep
from datetime import datetime
from send_email import send_email


def get_datetime():
    """
    Returns the current time.
    e.g. 17:47:15
    """
    return datetime.now().strftime("%H:%M:%S")


date = get_datetime()


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
    username = get_str_input().title()
    chatbot_message(
        f"Hi, {username}. Thank you for using our chat service.\n"
        "How may I assist you today?\n"
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


def get_int_input():
    """
    Returns the user input.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be a digit.
    The loop will continue to prompt the user until the data is valid.
    """

    while True:

        user_input = input("\n>> ")
        is_a_digit = validate_input(user_input, str.isdigit)

        if is_a_digit:
            break

    return log(int(user_input), "User")


def get_str_input():
    """
    Returns the user input.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be a string.
    The loop will continue to prompt the user until the data is valid.
    """

    while True:

        user_input = input("\n>> ").strip().lower()
        new_string = "".join(user_input.split())
        is_a_string = validate_input(new_string, str.isalpha)

        if is_a_string:
            break

    return log(user_input, "User")


def validate_input(user_input, str_method):
    """
    Validates the user input.
    Inside the try/except block, the user is prompted
    to enter the data type. Raises a ValueError if
    data type is not a digit or an alpha,
    depending to the data type specification
    by the user.
    """

    try:
        if not str_method(user_input):
            raise ValueError(f"\n'{user_input}' isn't a valid input.")

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

        print_menu()

        user_choice = get_int_input()

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
            chatbot_message(
                f"\nThis option does not exist in the menu. Please try again."
            )


def add_new_task():
    """
    Adds a new task to the list.
    """
    chatbot_message("What task would you like to add?")
    task = get_str_input()

    chatbot_message(f"Great! Let's add [{task.upper()}] to your list.")
    chatbot_message("\nAdding task...")

    task_list.append(task.capitalize())
    sleep(2)

    chatbot_message("\nTask added!")
    ask_to_add_task()


def view_all_tasks(list):
    """
    Prints a list of tasks.
    """
    if not list:
        sleep(1)
        chatbot_message("Your list is still empty.\n")
        ask_to_add_task()

    else:
        for i, task in enumerate(list):
            i += 1
            print(f"\t{i} - {task}")

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
        chatbot_message("Which task would you like to delete?")
        view_all_tasks(task_list)
        task_to_delete = get_int_input()

        for i, task in enumerate(task_list):

            if task_to_delete != i + 1:
                return chatbot_message("Task not found.\n")

            else:
                removed_task = task_list.pop(i)
                removed_items.append(removed_task)
                sleep(1)
                return chatbot_message(f"Task [{task}] removed!\n")


def restore_task():
    """
    Restores a removed task.
    """
    if not removed_items:
        sleep(1)
        chatbot_message("There is no tasks to be restored.\n")
        ask_to_add_task()

    else:
        chatbot_message("Which task would you like to restore?")
        view_all_tasks(removed_items)
        task_to_restore = get_int_input()

        for i, task in enumerate(removed_items):

            if task_to_restore != i + 1:
                return chatbot_message("Task not found.\n")

            else:
                restored_task = removed_items.pop(i)
                task_list.append(restored_task)
                sleep(1)
                return chatbot_message(f"Task [{task}] restored!\n")


def end_chat():
    """
    Prints a message to the user ending the conversation.
    """
    chatbot_message(
        "I'm glad I was able to get that sorted out for you."
        "\nBefore you go, would you like to get a copy of this chat? [y/N]"
    )

    answer = get_str_input()[0]

    if answer == "y":
        chatbot_message("Great! Enter your email address below:\n")
        email = log(input(">> "), "User")
        is_a_valid_email = send_email(email)

        if is_a_valid_email:

            sleep(3)
            print("\nSending email...\n")
            sleep(5)
            chatbot_message(
                "OK, all done! Check your inbox for an email "
                "with the LiveChat transcript.\n"
            )

        else:
            chatbot_message(
                "Sorry. It appears that you have not entered "
                "your email address correctly\n."
            )
    else:
        chatbot_message("Please enter a valid option.\n")
        return False

    chatbot_message(
        "\nThank you so much for using our chat service.\n"
        "We hope we will hear from you soon.\n"
        "Have a great day!\n"
    )
    sleep(2)
    os.remove("log.txt")
    print("\n>>> The agent has left the chat.")
    sleep(3)
    clear_output()
    sys.exit()


def ask_to_add_task():
    """
    Asks the user if he/she wants to add a new task.
    """
    chatbot_message("Would you like to add a new task? [y/N]")
    answer = get_str_input()[0]

    if answer == "y":
        add_new_task()

    else:
        chatbot_message("Okay, let me show you some other options.\n")
        # then loop goes back to the main thread (print_menu)


def log(message, person):
    """
    Logs the conversation and save to an external file.
    """
    path = "log.txt"

    with open(path, "a", newline="") as log_file:
        log_file.write(f"[{person}][{date}] - {message}\n")
        return message


def clear_output():
    """
    This function clears the output of the terminal
    right after the user exits the program.
    """
    return os.system("cls") if os.name == "nt" else os.system("clear")


def main():
    """
    Run all program functions.
    """
    greetings()
    start_bot()


removed_items = []
task_list = []
