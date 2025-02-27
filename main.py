from typing import Dict

from colorama import Fore, Back, Style

type Contacts = Dict[str, int]


def show_contacts(contacts: Contacts) -> str:
    return ", \n".join(f"{name}: {phone}" for name, phone in contacts.items())


def show_number(contacts: Contacts, name: str) -> str:
    return contacts[name]


def change_contact(args, contacts: Contacts) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts: Contacts) -> str:
    name, phone = args
    capitalized = name.capitalize()
    contacts[capitalized] = phone
    return "Contact added."


def main():
    contacts: Contacts = {}
    print(Fore.CYAN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.GREEN + "Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.WHITE + Back.BLACK + "Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        elif command == "phone":
            print(Fore.BLUE + show_number(contacts, args[0]))
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
