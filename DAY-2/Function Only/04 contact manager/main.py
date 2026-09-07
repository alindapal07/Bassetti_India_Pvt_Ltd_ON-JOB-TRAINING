# Contact Manager Main Program

from contacts import (
    add_contact,
    delete_contact,
    search_contact,
    update_contact,
    list_contacts
)

while True:
    print("\n===== CONTACT MANAGER =====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. List Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")

    try:
        # Add Contact
        if choice == "1":

            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            message = add_contact(name, phone, email)
            print(message)

        # Delete Contact
        elif choice == "2":
            name = input("Enter contact name: ")
            message = delete_contact(name)
            print(message)
        # Search Contact
        elif choice == "3":
            name = input("Enter contact name: ")
            contact = search_contact(name)

            print("\nContact Found")
            print("Name  :", contact["name"])
            print("Phone :", contact["phone"])
            print("Email :", contact["email"])
            
        # Update Contact
        elif choice == "4":

            name = input("Enter contact name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            message = update_contact(name, phone, email)
            print(message)
            
        # List Contacts
        elif choice == "5":
            list_contacts()
        # Exit
        elif choice == "6":
            print("Thank you for using Contact Manager!")
            break
        # Invalid menu choice
        else:
            print("Invalid choice. Please select 1-6.")

    except ValueError as e:
        print("Error:", e)