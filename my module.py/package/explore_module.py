import math
import random
import uuid
import datetime

def explore_menu():
    while True:
        print("\n===== Explore Module =====")
        print("1. math")
        print("2. random")
        print("3. uuid")
        print("4. datetime")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print(dir(math))
        elif choice == "2":
            print(dir(random))
        elif choice == "3":
            print(dir(uuid))
        elif choice == "4":
            print(dir(datetime))
        elif choice == "5":
            break
        else:
            print("Invalid Choice!")

