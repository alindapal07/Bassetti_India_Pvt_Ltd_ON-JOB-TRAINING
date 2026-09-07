# Contact Manager Operations


contacts = [
    {
        "name": "Tarun",
        "phone": "9876543210",
        "email": "tarun@example.com"
    }
]

# Add a new contact
def add_contact(name, phone, email):
    # Check phone
    if phone == "":
        raise ValueError("Phone number cannot be empty")

    # Check email
    if email == "":
        raise ValueError("Email cannot be empty")
    # Check duplicate contact
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            raise ValueError("Contact already exists")

    # Create contact
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    return "Contact added successfully"


# Delete a contact
def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            return "Contact deleted successfully"
    raise ValueError("Contact not found")


# Search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    raise ValueError("Contact not found")


# Update a contact
def update_contact(name, phone, email):
    if phone == "":
        raise ValueError("Phone number cannot be empty")
    if email == "":
        raise ValueError("Email cannot be empty")
    for contact in contacts:

        if contact["name"].lower() == name.lower():
            contact["phone"] = phone
            contact["email"] = email
            return "Contact updated successfully"
    raise ValueError("Contact not found")


# Display all contacts
def list_contacts():
    if len(contacts) == 0:
        print("No contacts available")
        return
    for contact in contacts:

        print("-------------------------")
        print("Name  :", contact["name"])
        print("Phone :", contact["phone"])
        print("Email :", contact["email"])
        print("-------------------------")