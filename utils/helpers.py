from models import employee
from models import store

employee=employee.employees()
def SaveEmployee():
    file=open("data\employees.txt","w")
    
    for employee in BasharLibrary.employee:
        file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")
        
    file.close()


def SaveProduct():
    file=open("data\employees.txt","w")
    
    for employee in BasharLibrary.employee:
        file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")
        
    file.close()


def SaveSalas():
    file=open("data\Salas.txt","w")
    
    for sale in BasharLibrary.sales:
        file.write(f"|{sale.sale_id}|{sale.name}|{sale.phone}|{sale.salary}\n")
        
    file.close()


    