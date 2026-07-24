"""
=========================================
Day 1 : CSV-Powered Contact Book
=========================================

A terminal-based contact management system
that stores contacts in a CSV file.

Features:
✔ Add a new contact
✔ View all contacts
✔ Search contacts by name
✔ Prevent duplicate names
✔ Partial name matching
✔ Automatically create contacts.csv

Concepts Covered:
✔ CSV File Handling
✔ Dictionaries
✔ Functions
✔ Loops
✔ Conditional Statements
✔ File Existence Checking
"""

import csv
import os

CONTACT_FILE = "contacts.csv"
CSV_HEADERS = ["Name", "Phone", "Email"]


# Step 1 : Create CSV File # 

def initialize_file():
    """Creates the contact file with headers if it doesn't exist."""

    if not os.path.exists(CONTACT_FILE):

        with open(
            CONTACT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)
            writer.writerow(CSV_HEADERS)


# Step 2 : Add New Contact # 

def add_contact():
    """Adds a new contact after checking for duplicate names."""

    name = input("Enter name : ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    # Prevent empty names from being added.
    if not name:
        print("❌ Name cannot be empty.")
        return

    # Check whether a contact with the same name already exists.
    with open(CONTACT_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for contact in reader:

            if contact["Name"].lower() == name.lower():

                print("❌ A contact with this name already exists.")
                return

    # Add the new contact to the CSV file.
    with open(
        CONTACT_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print(f"✅ Contact '{name}' added successfully!")


# Step 3 : View All Contacts # 

def view_contacts():
    """Displays all saved contacts in a table-like format."""

    with open(
        CONTACT_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)
        contacts = list(reader)

    if not contacts:
        print("\n📭 No contacts found.")
        return

    print("\n" + "=" * 70)
    print("📒 YOUR CONTACTS".center(70))
    print("=" * 70)

    print(f"{'Name':<20} {'Phone':<20} {'Email':<25}")
    print("-" * 70)

    for contact in contacts:

        print(
            f"{contact['Name']:<20} "
            f"{contact['Phone']:<20} "
            f"{contact['Email']:<25}"
        )

    print("=" * 70)


# Step 4 : Search Contact #

def search_contact():
    """Searches contacts using a partial or complete name."""

    search_term = input(
        "Enter name to search: "
    ).strip().lower()

    if not search_term:
        print("❌ Search term cannot be empty.")
        return

    found_contacts = []

    with open(
        CONTACT_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for contact in reader:

            # Partial matching allows searches like "ana"
            # to find contacts such as "Ananya".
            if search_term in contact["Name"].lower():
                found_contacts.append(contact)

    if not found_contacts:

        print("❌ No matching contacts found.")
        return

    print("\n🔍 SEARCH RESULTS")
    print("-" * 70)

    for contact in found_contacts:

        print(f"👤 Name : {contact['Name']}")
        print(f"📞 Phone: {contact['Phone']}")
        print(f"📧 Email: {contact['Email']}")
        print("-" * 70)


# Step 5 : Main Menu # 

def main():
    """Runs the main Contact Book application."""

    # Make sure the CSV file exists before using the app.
    initialize_file()

    while True:

        print("\n" + "=" * 40)
        print("📒 CONTACT BOOK".center(40))
        print("=" * 40)

        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input(
            "\nChoose an option (1-4): "
        ).strip()

        if choice == "1":

            add_contact()

        elif choice == "2":

            view_contacts()

        elif choice == "3":

            search_contact()

        elif choice == "4":

            print("\n👋 Thanks for using Contact Book!")
            break

        else:

            print("❌ Invalid choice. Please select 1-4.")


# Program Entry Point # 

if __name__ == "__main__":
    main()