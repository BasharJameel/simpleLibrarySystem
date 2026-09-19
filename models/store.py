from models.sale import sale
from models.employee import Employee
from models.saleitem import saleitem
from models.category import Category

class Store:

    def __init__(self,name):
        self.name=name
        self.Category=[]
        self.products=[]
        self.Employees=[]
        self.sales= []
        self.EmployeeCount=0
        self.ProductCount=0
        self.SalasProduct=0

    def AddEmployee(self, Employee_id, name, jobs, phone, salary):

         if (jobs == 'Manager'):
            self.Employees.append(Employee.Manager(Employee_id, name, jobs, phone, salary))
         elif (jobs == 'cashier'):
            self.Employees.append(Employee.Cashier(Employee_id, name, jobs, phone, salary))
         elif (jobs == 'storekeeper'):
            self.Employees.append(Employee.Storekeeper(Employee_id, name, jobs, phone, salary))


     
    def AddProduct(self, ID, Name, Price, Categories, Description, Status ):
       self.Products.append(Product( ID, Name, Price, Categories, Description, Status ))
     

    def CreatSale(self, Employee, payment):

        self.sales.append(sale(Employee, payment))
      

    def AddCategory(self,category_id,name,description):

        self.Category.append(Category(category_id,name,description))

        

    def DisplayProduct(self):
         print("--------------------------------------")
         print("          Product List                ")
         print("--------------------------------------")
         
         for Cate in self.Category:
         
           pritn(f"----{Cate}----")
  
           for product in self.products:
           
             if (product.category == Cate):
                  print(f"-{product.name}")
        

          
    def SearchProduct(self,SearchedProduct):
        for product in self.products:
          
            if (product.id==SearchedProduct):
                product.display_info()

    def DisplaySales(self,SearchSale):
         for Sales in self.sales:
          
            if (Sales.id==SearchSale):
                Sales.display_sale()
