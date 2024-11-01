contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_contacts():
    for name, details in contacts.items():
        print("Name:", name)
        print("Phone:", details['phone'])
        print("Email:", details['email'])
        print()

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
      
