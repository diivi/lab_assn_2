class Employee:
    def __init__(self, name, salary, age, e_id):
        self.name = name
        self.salary = salary
        self.age = age
        self.e_id = e_id

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Age: {self.age}, ID: {self.e_id}"
    
    def __repr__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Age: {self.age}, ID: {self.e_id}"
    

class EmployeeDB:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def delete_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.e_id == employee_id:
                self.employee_list.remove(employee)
                return True
        return False

    def display_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.e_id == employee_id:
                return employee
        return None

    def display_all(self):
        return self.employee_list

    def update_employee(self, employee_id, new_employee):
        for employee in self.employee_list:
            if employee.e_id == employee_id:
                employee.name = new_employee.name
                employee.salary = new_employee.salary
                employee.age = new_employee.age
                return True
        return False
    
    def sort_by(self, sort_by):
        if sort_by == "name":
            self.employee_list.sort(key=lambda x: x.name)
        elif sort_by == "salary":
            self.employee_list.sort(key=lambda x: x.salary)
        elif sort_by == "age":
            self.employee_list.sort(key=lambda x: x.age)
        elif sort_by == "id":
            self.employee_list.sort(key=lambda x: x.e_id)
        else:
            print("Invalid sort by value")
            return False
        return True
    

def main():
    db = EmployeeDB()
    while True:
        print("1. Add employee")
        print("2. Delete employee")
        print("3. Display employee")
        print("4. Display all employees")
        print("5. Update employee")
        print("6. Sort employees")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))
            age = int(input("Enter age: "))
            e_id = int(input("Enter ID: "))
            employee = Employee(name, salary, age, e_id)
            db.add_employee(employee)
        elif choice == 2:
            e_id = int(input("Enter ID: "))
            if db.delete_employee(e_id):
                print("Employee deleted")
            else:
                print("Employee not found")
        elif choice == 3:
            e_id = int(input("Enter ID: "))
            employee = db.display_employee(e_id)
            if employee:
                print(employee)
            else:
                print("Employee not found")
        elif choice == 4:
            employees = db.display_all()
            for employee in employees:
                print(employee)
        elif choice == 5:
            e_id = int(input("Enter ID: "))
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))
            age = int(input("Enter age: "))
            new_employee = Employee(name, salary, age, e_id)
            if db.update_employee(e_id, new_employee):
                print("Employee updated")
            else:
                print("Employee not found")
        elif choice == 6:
            sort_by = input("Enter sort by value: ")
            db.sort_by(sort_by)
        elif choice == 7:
            break
        else:
            print("Invalid choice")

            