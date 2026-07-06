import random
import string

def random_number():
    print("Random Number:", random.randint(1, 100))

def otp_generator():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)

def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "@#$%&*"
    password = "".join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

def dice_roll():
    print("Dice:", random.randint(1, 6))

def coin_toss():
    print("Result:", random.choice(["Heads", "Tails"]))

def random_name():
    names = ["Amit", "Priya", "Rahul", "Neha", "Riya", "Jay"]
    print("Selected Name:", random.choice(names))

def random_menu():
    while True:
        print("\n===== Random Menu =====")
        print("1. Random Number")
        print("2. OTP Generator")
        print("3. Password Generator")
        print("4. Dice Roll")
        print("5. Coin Toss")
        print("6. Random Name")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            random_number()
        elif choice == "2":
            otp_generator()
        elif choice == "3":
            password_generator()
        elif choice == "4":
            dice_roll()
        elif choice == "5":
            coin_toss()
        elif choice == "6":
            random_name()
        elif choice == "7":
            break
        else:
            print("Invalid Choice!")
