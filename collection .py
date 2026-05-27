students = []
all_subjects = set()


def add_student():

    student_id = input("Student ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")

    subjects_input = input("Subjects (comma-separated): ")

    subjects = [sub.strip() for sub in subjects_input.split(",")]

    for sub in subjects:
        all_subjects.add(sub)

    id_info = (student_id, dob)

    student = {
        "id_info": id_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    students.append(student)

    print("\nStudent added successfully!\n")


def display_students():

    if not students:
        print("No student records found.")
        return

    print("\n--- Display All Students ---")

    for student in students:

        student_id = student["id_info"][0]

        print(
            f"Student ID: {student_id} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']} | "
            f"Subjects: {', '.join(student['subjects'])}"
        )


def update_student():

    student_id = input("Enter Student ID to update: ")

    for student in students:

        if student["id_info"][0] == student_id:

            new_age = int(input("Enter new age: "))

            new_subjects = input("Enter new subjects (comma-separated): ")

            subject_list = [s.strip() for s in new_subjects.split(",")]

            student["age"] = new_age
            student["subjects"] = subject_list

            for sub in subject_list:
                all_subjects.add(sub)

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():

    student_id = input("Enter Student ID to delete: ")

    for i in range(len(students)):

        if students[i]["id_info"][0] == student_id:

            del students[i]

            print("Student deleted successfully!")
            return

    print("Student not found.")


def display_subjects():

    print("\n--- Subjects Offered ---")

    for subject in all_subjects:
        print(subject)


def menu():

    while True:

        print("\n===== Student Data Organizer =====")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_subjects()

        elif choice == "6":
            print("Thank you for using Student Data Organizer!")
            break

        else:
            print("Invalid choice.")


menu()
