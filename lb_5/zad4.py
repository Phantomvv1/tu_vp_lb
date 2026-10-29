contacts: dict[str, str] = {}

for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

search_name = input("Enter a name to search: ")

if search_name in contacts:
    print("Phone number: ", contacts[search_name])
else:
    print("Contact not found")
