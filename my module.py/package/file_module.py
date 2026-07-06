def create_file():
    filename = input("Enter file name: ")
    with open(filename, "w") as file:
        print("File created successfully.")

def write_file():
    filename = input("Enter file name: ")
    text = input("Enter text: ")

    with open(filename, "w") as file:
        file.write(text)

    print("Data written successfully.")

def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

def append_file():
    filename = input("Enter file name: ")
    text = input("Enter text to append: ")

    with open(filename, "a") as file:
        file.write("\n" + text)

    print("Data appended successfully.")

def file_menu():
    while True:
        print("\n===== File Menu =====")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid Choice!")
