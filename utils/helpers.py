from models.employee import Employee

<<<<<<< HEAD
employee=employee.employees()
def SaveEmployee():
    file=open("data\employees.txt","w")
    
    for employee in BasharLibrary.employee:
        file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")
        
    file.close()
=======
def SaveEmployee(employees):
    with open("data/employees.txt", "w") as file:
        for employee in employees:
            file.write(f"|{employee.employee_id}|{employee.name}|{employee.phone}|{employee.salary}\n")

>>>>>>> 63db42e8c31dd4199f445220d48d93ad86a5a161


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


    