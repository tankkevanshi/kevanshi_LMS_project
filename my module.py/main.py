from package.datetime_module import datetime_menu
from package.math_module import math_menu
from package.random_module import random_menu
from package.uuid_module import uuid_menu
from package.file_module import file_menu
from package.explore_module import explore_menu

def main():
    while True:
        print("\n========== Multi-Utility Toolkit ==========")
        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. UUID Generation")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_menu()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
