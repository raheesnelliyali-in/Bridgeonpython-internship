contacts = {}

while True:
    print("\n    Contact Book    ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print(f"{name} added successfully.")
        print("1. Add Contact")

    elif choice == "2":
        name = input("Enter name to search: ")
        phone = contacts.get(name)
        if phone:
            print(f"{name}'s phone number is {phone}")
        else:
            print(f"{name} not found.")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            contacts[name] = phone
            print(f"{name} updated successfully.")
        else:
            print(f"{name} not found.")
            
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully.")
        else:
            print(f"{name} not found.")

    elif choice == "5":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContacts (Sorted):")
            for name in sorted(contacts):
                print(f"{name} : {contacts[name]}")

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")