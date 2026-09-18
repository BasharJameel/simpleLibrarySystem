from models import employee
from models import store

employee=employee.employees()
def SaveEmployee(employees):
    file=open("data\employees.txt","w")
    
    for employee in BasharLibrary.employee:
        file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")
        
    file.close()


    