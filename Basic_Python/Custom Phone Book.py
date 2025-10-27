contact = []
def add_contact():
    name = input("Enter your name:")
    phone_num = int(input("Enter your phone number:"))

    contacts = {
        'name' : name,
        'phone' : phone_num
}
    contact.append(contacts)
    print("contact addes")

def view_contact():
    if not contact:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for c in contact:
            print(f"Name: {c['name']}, Phone: {c['phone']}")

def view_name():
    by_name = input("search a person by name:").lower()
    found = False
    for c in contact:
        if  c['name'].lower() == by_name:
            print(f"Found: Name:{c['name']}, phone: {c['phone']}")
            found = True
            break
    if not found:
        print("Contact not found")
def delet_contact():
    delete_by_name = input("enter a contact name:")
    found = False
    for c in contact:
        if c['name'] == delete_by_name:
            contact.remove(c)
            view_contact()
            found = True
            break
    if not found:
        print("Inavalid contact")

while True:
    print("----------CONTACT LIST --------------")
    print(" 'press' : (1) if you want to add contact:")
    print(" 'press' : (2) if you want to view contacts:")
    print("'press' : (3) if you want to search contact by Name:")
    print("'press' : (4) if you want to delete contact by Name:")
    print("'press' : (5) if you want to exit:")

    choice = input("Enter a choice:")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        view_name()
    elif choice == '4':
        delet_contact()
    elif choice == '5':
        print("GOOD BY")
        break
    else:
        print("invaild characters:")


