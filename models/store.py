from models import sale

class store:

    def __init__(self,name):
        self.name=name
        self.product=[]
        self.employee=[]
        self.sales= []

    employeeCount=0
    ProductCount=0

    def AddEmployee(self, EmployeeID, EmployeeName, Phone, Salary):

        self.employee[employee_Count]=Employee( EmployeeID, EmployeeName, Phone, Salary)

        employee_Count+=1

    def AddProduct(self, ID, Name, Price, Categories, Description, Status ):
        self.Product[ProductCount]=Product( ID, Name, Price, Categories, Description, Status )


    def CreatSale(self, employee, payment):
        



    

