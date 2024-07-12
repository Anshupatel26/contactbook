#!/usr/bin/env python
# coding: utf-8

# In[ ]:


contact = {}

def display_contact():
    if not contact:
        print("Empty contact book")
    else:
        print("Name\t\tContact Number")
        for key, value in contact.items():
            print("{}\t\t{}".format(key, value))

while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add a contact")
    print("2. Search a contact")
    print("3. Display all contacts")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
        print("Contact added successfully!")
    
    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            print("{}'s contact number is {}".format(search_name, contact[search_name]))
        else:
            print("Name is not found in contact book")
    
    elif choice == 3:
        display_contact()
    
    elif choice == 4:
        edit_name = input("Enter the contact name to edit: ")
        if edit_name in contact:
            new_phone = input("Enter the new mobile number: ")
            contact[edit_name] = new_phone
            print("Contact updated successfully!")
            display_contact()
        else:
            print("Name is not found in contact book")
    
    elif choice == 5:
        del_name = input("Enter the contact name to delete: ")
        if del_name in contact:
            confirm = input("Are you sure you want to delete this contact? (y/n): ")
            if confirm.lower() == 'y':
                contact.pop(del_name)
                print("Contact deleted successfully!")
                display_contact()
        else:
            print("Name is not found in contact book")
    
    elif choice == 6:
        print("Exiting the contact book. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:




