from models import sale
from models import employee

class store:

    def __init__(self,name):
        self.name=name
        self.Category=[]
        self.product=[]
        self.employee=[]
        self.sales= []
        employeeCount=0
        ProductCount=0
        SalasProduct=0

    def AddEmployee(self, employee_id, name, jobs, phone, salary):

         if (jobs == 'Manager'):
            self.employee[employee_Count]=employee.Manager(employee_id, name, jobs, phone, salary)
         elif (jobs == 'cashier'):
            self.employee[employee_Count]=employee.Cashier(employee_id, name, jobs, phone, salary)
         elif (jobs == 'storekeeper'):
            self.employee[employee_Count]=employee.Storekeeper(employee_id, name, jobs, phone, salary)

         employee_Count+=1 


     
    def AddProduct(self, ID, Name, Price, Categories, Description, Status ):
        self.Product[ProductCount]=Product( ID, Name, Price, Categories, Description, Status )
        ProductCount+=1

    def CreatSale(self, employee, payment):

        self.sales[SalasProduct]=sale.sale(employee, payment)
        SalasProduct+=1

    def AddCategory(self):
        pass

    def DisplayProduct():
        pass

   




    




    

