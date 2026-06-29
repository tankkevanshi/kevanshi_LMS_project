# Journal Manager Program

import os
from datetime import datetime


class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Add New Entry
    def add_entry(self):
        entry = input("\nEnter your journal entry:\n")

        with open(self.filename, "a") as file:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"\n[{timestamp}]\n")
            file.write(entry + "\n")
            file.write("-" * 40 + "\n")

        print("\nEntry added successfully!")

    # View All Entries
    def view_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries found.")
            return

        with open(self.filename, "r") as file:
            print("\n========== JOURNAL ==========\n")
            print(file.read())

    # Search Entry
    def search_entry(self):
        if not os.path.exists(self.filename):
            print("\nJournal file not found.")
            return

        word = input("Enter keyword to search: ")

        with open(self.filename, "r") as file:
            data = file.read()

            if word.lower() in data.lower():
                print("\nKeyword Found!\n")
                print(data)
            else:
                print("\nKeyword Not Found.")

    # Delete Journal File
    def delete_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("\nJournal file deleted successfully.")
        else:
            print("\nJournal file does not exist.")


# Main Program
journal = JournalManager()

while True:

    print("\n========== Journal Manager ==========")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete Journal File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_file()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
