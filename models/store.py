from models.sale import sale
from models.employee import Employee
from models.saleitem import saleitem
from models.category import Category
from models.product import *
from models.payment import *


class Store:

    def __init__(self,name):
        self.Name=name
        self.Category=[]
        self.products=[]
        self.Employees=[]
        self.sales= []
        self.EmployeeCount=0
        self.ProductCount=0
        self.SalasProduct=0

    def AddEmployee(self, Employee_id, name, phone, salary, jobs=1):
         print(jobs)
         if (int(jobs) == 1):
         
            self.Employees.append(Employee(Employee_id, name, jobs, phone, salary))

         elif (int(jobs)  == 2):
            self.Employees.append(Employee(Employee_id, name, jobs, phone, salary))
         elif (int(jobs)  == 3):
            self.Employees.append(Employee(Employee_id, name, jobs, phone, salary))


     
    def AddProduct(self, ID, Name, Price, Categories, Description, Status ):
       self.products.append(Product( ID, Name, Price, Categories, Description, Status ))
     

    def CreatSale(self, Employee, payment):
        sale =sale(Employee,payment)

        sale.create_saleitem()

        process_payment(sale.calculate_total())


        
        

        self.sales.append(sale(Employee))
      

    def AddCategory(self):
        print("="*10)
        category_id=input("Enter Categorey ID ")
        name=input("Enter Categorey Name")
        description=input("Enter Categorey Descriiption")
        self.Category.append(Category(category_id,name,description))
        print("-"*10)
        print("New Category has been add ")

        

    def DisplayProductByCategory(self):
         print("--------------------------------------")
         print("      Product List  ByCategory              ")
         print("--------------------------------------")
         
         for Cate in self.Category:
         
           print(f"----{Cate}----")
  
           for product in self.products:
           
             if (product.category == Cate):
                  print(f"-{product.name}")
        
    def DisplayProduct(self):
         print("--------------------------------------")
         print("          Product List                ")
         print("--------------------------------------")
         
         for product in self.products:
          print(f"-{product.name}")
        

          
    def SearchProduct(self):
       
        SearchedProduct=input("Enter  Product ID That you wante to Search aboute")
        i=1
      
        for product in self.products:
          
            if (str(product.product_id)==SearchedProduct):
                product.display_info()
                i=0
        if (i):
            print("there is no product has this id")
               

    def SearchEmployee(self,SearchedEmployee):
        SearchedEmployee=input("Enter  Employee ID That you wante to Search aboute")

        for Employee in self.Employees:
          
            if (Employee.id==SearchedEmployee):
                product.display_info()

    def DisplaySales(self,SearchSale):
        SearchSale=input("Enter  Salae ID That you wante to Delete it >")

        for Sales in self.sales:
            if (Sales.id==SearchSale):
                Sales.display_sale()



