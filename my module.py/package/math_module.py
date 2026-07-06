import math

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    ch = input("Choose operation: ")

    if ch == "1":
        print("Answer =", a + b)
    elif ch == "2":
        print("Answer =", a - b)
    elif ch == "3":
        print("Answer =", a * b)
    elif ch == "4":
        if b != 0:
            print("Answer =", a / b)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid Choice!")

def factorial():
    n = int(input("Enter a number: "))
    print("Factorial =", math.factorial(n))

def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)

    print("sin =", math.sin(rad))
    print("cos =", math.cos(rad))
    print("tan =", math.tan(rad))

def logarithm():
    n = float(input("Enter number: "))
    print("Log =", math.log10(n))

def area_circle():
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print("Area =", area)

def compound_interest():
    p = float(input("Principal Amount: "))
    r = float(input("Rate (%): "))
    t = float(input("Time (Years): "))

    amount = p * (1 + r/100) ** t
    ci = amount - p

    print("Compound Interest =", round(ci, 2))
    print("Total Amount =", round(amount, 2))

def math_menu():
    while True:
        print("\n===== Math Menu =====")
        print("1. Calculator")
        print("2. Factorial")
        print("3. Trigonometry")
        print("4. Logarithm")
        print("5. Area of Circle")
        print("6. Compound Interest")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            factorial()
        elif choice == "3":
            trigonometry()
        elif choice == "4":
            logarithm()
        elif choice == "5":
            area_circle()
        elif choice == "6":
            compound_interest()
        elif choice == "7":
            break
        else:
            print("Invalid Choice!")
