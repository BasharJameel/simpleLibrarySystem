from models import employee 
from models import store



def SaveProduct(Products):
    file=open("data\product.txt","w")
    
    for Product in Products :
        file.write(f"|{Product.product_id}|{Product.name}|{Product.price}|{Product.category}|{Product.description}|{Product.status}\n")
  
        
    file.close()



def LoadProduct(Library):

    with open("data/product.txt",'r') as file:

        for line in file:
            data=line.strip().split('|')

            product_id=int(data[1])
            name=data[2]
            price=int(data[3])
            category=data[4]
            description=data[5]
            status=data[6]

            Library.AddProduct(product_id, name, price, category, description, status)


            


def SaveSalas(Sales):
    file = open("data/Salas.txt", "w")

    for sale in Sales:
        items_data = []

        for item in sale.items:
            items_data.append(
                f"{item.product_id}:{item.quantity}:{item.price_unit}"
            )

        file.write(
            f"|{sale.sale_id}|"
            f"{sale.date}|"
            f"{sale.employee.employee_id}|"
            f"{sale.total}|"
            f"{','.join(items_data)}|"
            f"{sale.payment}\n"
        )

    file.close()



def LoadSalas(Library, Employees):

    with open("data/Salas.txt", "r") as file:

        for line in file:
            data = line.strip().split('|')

            sale_id = int(data[1])
            date = data[2]
            employee_id = int(data[3])
            total = float(data[4])
            payment = data[6]

            items = []

            for item_data in data[5].split(','):
                item = item_data.split(':')

                product_id = int(item[0])
                quantity = int(item[1])
                price_unit = float(item[2])

                items.append(
                    saleitem(product_id, quantity, price_unit)
                )

            employee = None

            for emp in Employees:
                if emp.employee_id == employee_id:
                    employee = emp
                    break

            Library.AddSale( sale_id, date, employee, items, total, payment )



def SaveEmployee(Employees):
    with open("data\employees.txt",'w') as file:
        for Employee in Employees:
           file.write(f"|{Employee.employee_id}|{Employee.name}|{Employee.phone}|{Employee.salary}\n")
    file.close ()      


def LoadEmployee(Library):

    with open("data/employees.txt", 'r') as file:

        for line in file:
            data = line.strip().split('|')

            employee_id = int(data[1])
            name = data[2]
            phone = data[3]
            salary = float(data[4])

            Library.AddEmployee(employee_id,name,phone,salary)

            
   

        


    