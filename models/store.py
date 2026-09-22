from models.sale import sale,create_saleitem, calculate_total
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
     

    def CreatSale(self, Employee):
        listSale =create_saleitem(self.products)
        total_sale=calculate_total(listSale) 
        payment=process_payment(total_sale)

        sale2=sale(Employee,payment,listSale,total_sale)
        sale2.display_sale("Ahmed",self.products)
        self.sales.append(sale2)
    

    

    def AddCategory(self):
        print("="*10)
        category_id=input("Enter Categorey ID ")
        name=input("Enter Categorey Name")
        description=input("Enter Categorey Descriiption")
        self.Category.append(Category(category_id,name,description))
        print("-"*10)
        print("New Category has been add ")


    def DisplayCategory(self):
        print("--------------------------------------")
        print("            Display Category          ")
        print("--------------------------------------")
        for Cate in self.Category:
            print(f"-   {Cate.name}")


    def DisplayProductByCategory(self):
         print("--------------------------------------")
         print("      Product List  ByCategory        ")
         print("--------------------------------------")
         
         for Cate in self.Category:
         
           print(f"----{Cate.name}----")
           
  
           for product in self.products:
           
             if (product.category == Cate.name):
                  print(f"-{product.name}")
        
    def DisplayProduct(self):
         print("--------------------------------------")
         print("          Product List                ")
         print("--------------------------------------")
         
         for product in self.products:
          print(f"-{product.name}")
        

          
    def SearchProduct(self):
       
        SearchedProduct=input("Enter  Product ID That you wante to Search aboute")
        found=False
      
        for product in self.products:
          
            if (str(product.product_id)==SearchedProduct):
                product.display_info()
                found=True
        if (not found):
            print("There is no product has this id")
               

    def SearchEmployee(self):
        SearchedEmployee=input("Enter  Employee ID That you wante to Search aboute")
        found =False
    
        for Employee in self.Employees:
          
            if (str(Employee.employee_id)==SearchedEmployee):
                 Employee.display_info()
                 found=True
        if not found:
            print("there is no such this id")
    def DisplaySale(self):
        SearchSale=input("Enter  Salae ID That you wante to search it :")

        for Sales in self.sales:
            if (str(Sales.sale_id)==str(SearchSale)):
                 Sales.display_sale("Ahmed",self.products)



