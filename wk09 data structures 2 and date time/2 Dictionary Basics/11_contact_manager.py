# Program to manage phone contacts
# Example of a dictionary

contacts = {} # empty dictionary

while True:
    choice = input("[D]isplay [A]dd [E]dit [R]emove [S]earch [Q]uit: ").strip().lower()

    match choice.lower()[0]:
        case "q":
            break # exit the loop

        case "d":
            if contacts:
                print(f"Number of Contacts: {len(contacts)}")
                print(f"{'Name':<12 {'Number'}}")
                for name, number in sorted(contacts.items()):
                    print(f"{name:<12} {number}")
            else:
                print("No contacts")

        case "a": # Add a new contact
            name = input("Enter a name of a new contact: ").strip() # remove any spaces at beginning or end
            number = input("Enter new phone number: ").strip()

            if name in contacts:
                print(f"{name} already in contacts")
            else:
                contacts[name] = number
        
        case "e": # Edit existing contact
            name = input("Enter name of contact to edit: ").strip()
            if name in contacts:
                number = input("Enter new phone number: ").strip()
                contacts[name] = number # update contact
            else:
                print(f"No such contact: {name}")

        case "r": # Remove contact
            name = input("Enter name of contact to remove: ").strip()

            # Pythonic deletion without exception (no need for exception handling)
            if contacts.pop(name, None) is None:
                print(f'No such contact: {name}')

        case "s": # Search for a single contact
            name = input("Enter name to search: ").strip()

            number = contacts.get(name)
            if number is not None: # If we got something back
                print(f"{name:<12} {number}")
            else:
                print(f"No such contact: {name}")

        case _:
            print("Invalid choice")