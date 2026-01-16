
class Employee:
    def __init__(self, employee_id=None, name=None, age=None, salary=0.0):
        self.__employee_id = employee_id 
        self.name = name
        self.age = age
        self.__salary = salary

    
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print(f"Employee Details:\nName: {self.name}\nAge: {self.age}\n"
              f"Employee ID: {self.__employee_id}\nSalary: ${self.__salary}")



class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")



class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")



def main():
    employees = []

    while True:
        print("--- Python OOP Project: Employee Management System ---")
        print("1. Create an Employee")
        print("2. Create a Manager")
        print("3. Create a Developer")
        print("4. Show Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            emp = Employee(emp_id, name, age, salary)
            employees.append(emp)
            print("Employee created successfully!")

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            mgr = Manager(emp_id, name, age, salary, dept)
            employees.append(mgr)
            print("Manager created successfully!")

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            dev = Developer(emp_id, name, age, salary, lang)
            employees.append(dev)
            print("Developer created successfully!")

        elif choice == "4":
            for emp in employees:
                emp.display()
                print("-" * 40)

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()
