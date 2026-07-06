from datetime import datetime
import time

def show_datetime():
    now = datetime.now()
    print("\nCurrent Date:", now.strftime("%Y-%m-%d"))
    print("Current Time:", now.strftime("%H:%M:%S"))

def date_difference():
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")

    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    diff = abs((d2 - d1).days)
    print("Difference:", diff, "days")

def format_date():
    now = datetime.now()
    print("\n1. DD-MM-YYYY")
    print("2. Month DD, YYYY")
    choice = input("Choose format: ")

    if choice == "1":
        print(now.strftime("%d-%m-%Y"))
    elif choice == "2":
        print(now.strftime("%B %d, %Y"))
    else:
        print("Invalid choice")

def countdown():
    sec = int(input("Enter countdown seconds: "))
    while sec > 0:
        print(sec)
        time.sleep(1)
        sec -= 1
    print("Time's Up!")

def stopwatch():
    input("Press Enter to Start...")
    start = time.time()
    input("Press Enter to Stop...")
    end = time.time()
    print("Elapsed Time:", round(end - start, 2), "seconds")

def datetime_menu():
    while True:
        print("\n===== Date & Time Menu =====")
        print("1. Show Current Date & Time")
        print("2. Date Difference")
        print("3. Format Date")
        print("4. Countdown")
        print("5. Stopwatch")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            show_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            countdown()
        elif choice == "5":
            stopwatch()
        elif choice == "6":
            break
        else:
            print("Invalid Choice!")
