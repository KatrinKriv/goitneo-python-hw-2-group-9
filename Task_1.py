def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def is_valid_phone(phone):
    return phone.isdigit()


@input_error
def add_contact(args, contacts):
    name, phone = args
    if not is_valid_phone(phone):
        raise ValueError
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    if not is_valid_phone(new_phone):
        raise ValueError
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}  # Dictionary to store contacts

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
