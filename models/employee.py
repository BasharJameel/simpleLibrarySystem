from abc import ABC, abstractmethod

class Employee():

    employee_count = 0

    def __init__(self, employee_id, name, phone, salary, jobs):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.jobs=jobs
        self.__salary = salary

        Employee.employee_count += 1

    @abstractmethod
    def work(self):
        pass

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary

    def update_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary
        print(f"Salary updated for {self.name}. New salary: {self.__salary}")

    def display_info(self):
        print("______________________")
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Phone       : {self.phone}")
        print(f"Role        : {self.__class__.__name__}")
        print(f"Salary      : {self.__salary}")
        print("_________________________")

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

class Manager(Employee):

    def __init__(self, employee_id, name, phone, salary, department=None):
        super().__init__(employee_id, name, phone, salary)
        self.department = department

    def work(self):
        print(f"{self.name} (Manager) is supervising store operations "
              f"and managing employees.")

    def manage_employees(self):
        print(f"{self.name} is managing the employees in the store.")

class Cashier(Employee):

    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary)

    def work(self):
        print(f"{self.name} (Cashier) is working at the register, "
              f"processing customer sales.")

    def process_sale(self, sale=None):
        print(f"{self.name} is processing a sale.")
        return sale

class Storekeeper(Employee):

    def __init__(self, employee_id, name, phone, salary):
        super().__init__(employee_id, name, phone, salary)


def create_employee():
      print("\nChoose employee type:")
      print("1. Manager")
      print("2. Cashier")
      print("3. Storekeeper")
      jobs = input("Enter choice (1-3): ")
      employee_id = int(input("Employee ID: "))
      name = input("Name: ")
      phone = input("Phone: ")
      salary = float(input("Salary: "))
      data =[ employee_id, name, jobs, phone, salary]

      return data

if __name__ == "__main__":

    def create_employee():
        print("\nChoose employee type:")
        print("1. Manager")
        print("2. Cashier")
        print("3. Storekeeper")
        jobs = input("Enter choice (1-3): ")

        employee_id = int(input("Employee ID: "))
        name = input("Name: ")
        phone = input("Phone: ")
        salary = float(input("Salary: "))
        data =[ employee_id, name, phone, salary]

        return data


    employees = []
    how_many = int(input("How many employees do you want to add? "))

    for i in range(how_many):
        emp = create_employee()
        employees.append(emp)

    print("\n===== Employee List =====")
    for emp in employees:
        emp.display_info()
        emp.work()
        print()

    print("Total employees created:", Employee.get_employee_count())
