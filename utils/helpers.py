from models.employee import Employee

def SaveEmployee(employees):
    with open("data/employees.txt", "w") as file:
        for employee in employees:
            file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")



    