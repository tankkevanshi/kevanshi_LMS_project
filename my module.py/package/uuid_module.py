import uuid

def generate_uuid():
    print("\nGenerated UUID:")
    print(uuid.uuid4())

def uuid_menu():
    while True:
        print("\n===== UUID Menu =====")
        print("1. Generate UUID")
        print("2. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_uuid()
        elif choice == "2":
            break
        else:
            print("Invalid Choice!")
