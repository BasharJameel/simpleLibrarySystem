from models.sale import sale
from models.employee import Employee
from models.saleitem import saleitem

class store:

    def __init__(self,name):
        self.name=name
        self.Category=[]
        self.product=[]
        self.Employee=[]
        self.sales= []
        self.EmployeeCount=0
        self.ProductCount=0
        self.SalasProduct=0

    def AddEmployee(self, Employee_id, name, jobs, phone, salary):

         if (jobs == 'Manager'):
            self.Employee.append(Employee.Manager(Employee_id, name, jobs, phone, salary))
         elif (jobs == 'cashier'):
            self.Employee.append(Employee.Cashier(Employee_id, name, jobs, phone, salary))
         elif (jobs == 'storekeeper'):
            self.Employee.append(Employee.Storekeeper(Employee_id, name, jobs, phone, salary))

         self.EmployeeCount+=1 


     
    #def AddProduct(self, ID, Name, Price, Categories, Description, Status ):
     #   self.Product[ProductCount]=Product( ID, Name, Price, Categories, Description, Status )
      #  ProductCount+=1

    def CreatSale(self, Employee, payment):

        self.sales.append(sale(Employee, payment))
        self.SalasProduct+=1

    def AddCategory(self):
        pass

    def DisplayProduct(self):
        pass

   




    




    

