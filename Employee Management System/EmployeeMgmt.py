class Employee:
    def __init__(self, name, age, designation, salary=None):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary if salary is not None else self.set_salary()

    def set_salary(self):
        if self.designation == "Programmer":
            return 25000
        elif self.designation == "Manager":
            return 30000
        elif self.designation == "Tester":
            return 20000

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}")

    def raise_salary(self, amount):
        self.salary += amount

    def to_text(self):
        return f"{self.name},{self.age},{self.designation},{self.salary}"


def save_to_file(employees, filename="employees.txt"):
    with open(filename, "w") as f:
        for emp in employees.values():
            f.write(emp.to_text() + "\n")


def main():
    employees = {}

    while True:
        print("\n1. Create\n2. Display\n3. Raise Salary\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                name = input("Enter name: ")
                if name in employees:
                    print("Employee already exists.")
                    continue

                age = input("Enter age: ")
                designation = input("Enter designation (Programmer / Manager / Tester): ")

                if designation not in ['Programmer', 'Manager', 'Tester']:
                    print("Invalid designation. Try again.")
                    continue

                emp = Employee(name, age, designation)
                employees[name] = emp

                save_to_file(employees)

                more = input("Do you want to add another employee? (yes/no): ")
                if more.lower() != 'yes':
                    break

        elif choice == '2':
            if not employees:
                print("No employees to display.")
            else:
                for emp in employees.values():
                    emp.display()

        elif choice == '3':
            if not employees:
                print("No employees to raise salary.")
            else:
                name = input("Enter the name of the employee to raise salary: ")
                if name in employees:
                    try:
                        amount = int(input("Enter the amount of salary increment: "))
                        employees[name].raise_salary(amount)
                        print(f"Salary raised for {name}. New salary: {employees[name].salary}")
                        save_to_file(employees)
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("Employee not found.")

        elif choice == '4':
            print("Thank you for using the system.")
            save_to_file(employees)
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
