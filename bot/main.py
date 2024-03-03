# from address_book import AddressBook, Field, Name, Phone, Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Incomplete command."

    return inner

@input_error
def add_contact(args, contacts):
    username, phone = args
    if username in contacts:
        return 'This name was added. Please enter another name or use the command "change".'
    if phone in contacts.values():
        return f"This number was saved with another name."
    if not (2 <= len(username) <= 12):
        return 'Enter the correct name from 2 to 12 characters.'
    if not phone.isdigit() or not (5 <= len(phone) <= 12):
        return 'Enter the correct phone in number format from 5 to 12 characters.'    
    
    else:
        contacts[username] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    username, phone = args
    if not username in contacts:
        return 'There is no contact with the specified name.'
    if phone in contacts.values():
        return f"This number was saved with another name."
    if not phone.isdigit() or not (5 <= len(phone) <= 12):
        return 'Enter the correct phone in number format from 5 to 12 characters.'  
    else:
        contacts[username] = phone
        return "Contact updated."

@input_error          
def show_phone(args, contacts):
    username = args[0]
    if username in contacts:
        return contacts[username]
    else:
        return 'There is no contact with the specified name.'

def show_all(contacts):
    if contacts:
       return '\n'.join([f"{name} : {phone}" for name, phone in contacts.items()])
    else:
       return 'Your contact list is empty.' 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()