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


def SaveSalas(Sales):
    file=open("data\Salas.txt","w")


    for sale in Sales:
        items_data=[]

        for item in sale.items:
            items_data.append(
                f"{item.product_id}:{item.quantity}:{price_unit}")
            
            file.write(f"|{sale.sale_id}|{sale.date}|{sale.employee}|{sale.total}|{','.join(items_data)}|{sale.payment.payment_id}")

    
    file.close()


    