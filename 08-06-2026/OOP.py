# 
class Employee:
    company = "ABC Technologies"

    def __init__(self, emp_id=0, name="Unknown", age=0, salary=0):
        self.__emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def display(self):
        print("\n----- Employee Details -----")
        print("Employee ID :", self.__emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self.__salary)

    def __del__(self):
        print(f"Employee {self.name} Removed")


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department  :", self.department)
        print("Role        :", Manager)


class Developer(Employee):
    def __init__(self, emp_id, name, age, salary, language):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language    :", self.language)
        print("Role        : Developer")


employees = []


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, age, salary)
    employees.append(emp)

    print("Employee Added Successfully")


def add_manager():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    mgr = Manager(emp_id, name, age, salary, department)
    employees.append(mgr)

    print("Manager Added Successfully")


def add_developer():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Salary: "))
    language = input("Enter Programming Language: ")

    dev = Developer(emp_id, name, age, salary, language)
    employees.append(dev)

    print("Developer Added Successfully")


def display_all():
    if len(employees) == 0:
        print("No Records Found")
    else:
        for emp in employees:
            emp.display()


def search_employee():
    eid = int(input("Enter Employee ID to Search: "))

    found = False

    for emp in employees:
        if emp.get_emp_id() == eid:
            emp.display()
            found = True
            break

    if not found:
        print("Employee Not Found")


def update_salary():
    eid = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.get_emp_id() == eid:
            newsalary = float(input("Enter New Salary: "))
            emp.set_salary(newsalary)
            print("Salary Updated")
            return

    print("Employee Not Found")


def delete_employee():
    eid = int(input("Enter Employee ID: "))

    for emp in employees:
        if emp.get_emp_id() == eid:
            employees.remove(emp)
            print("Employee Deleted")
            return

    print("Employee Not Found")


print("Is Manager subclass of Employee ?",
      issubclass(Manager, Employee))

print("Is Developer subclass of Employee ?",
      issubclass(Developer, Employee))


while True:
    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Display All Employees")
    print("5. Search Employee")
    print("6. Update Salary")
    print("7. Delete Employee")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        add_manager()

    elif choice == 3:
        add_developer()

    elif choice == 4:
        display_all()

    elif choice == 5:
        search_employee()

    elif choice == 6:
        update_salary()

    elif choice == 7:
        delete_employee()

    elif choice == 8:
        print("Thank You")
        break
    else:
        print("Invalid Choice")

    print("Thank you")


    
        
                
    
