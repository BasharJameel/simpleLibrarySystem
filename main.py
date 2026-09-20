from utils.display import PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintSalesMenu, PrintReportsMenu
from utils.display import PrintEmployeeDisplayHeader, PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintSalesMenu, PrintReportsMenu
from models.store import *
from utils.helpers import *
from GUI.CreateAnewProducteInterface import *
from models.employee import *
import os
from models.payment import *



            

def main():
    #ask to enter the name of employee and check from file of employee 
    #store it in متغير to add it in saleitem and sale

    # def employee_enter():
    #     while True:
    #         employee_name=input("enter your name :")
    #         for em in Library.products:
    #              if employee_name==em.name:
    #                 print(f"hi? {employee_name}")
    #                 return employee_name

    #              else:print("you are not in the system")

    # name=employee_enter()
    
   
    Library=Store("basharstore")

    LoadEmployee(Library)
    LoadProduct(Library)
    # employee_enter(Library)
    
    
    def products_process():

        PrintProductMenu()
   
        print(f"{Library.Employees[0].name}")
        choice=int(input("enter your choice:"))
        while True:
            
            match choice:
                case 1:
                    os.system("cls")
                    productData = AddProductGUI()
                    Library.AddProduct(productData[0],productData[1],productData[2],productData[3],productData[4],productData[5] )
                    PrintProductMenu()

                case 2:
                   os.system("cls")
                   Library.DisplayProduct()

                case 3:
                    i='Y'
                    while(i=="Y" or i=='y'):

                     os.system("cls")
                     Library.SearchProduct()
                     i=input("Do you wante to enter search agine Y/N")
                case 4:
                    SearchedProduct=input("Enter product ID ")
                    
                    for product in Library.products:
        
                        if (str(product.product_id)==SearchedProduct):
                             price=int(input("Enter the new price"))
                             product.update_price(price)
                             print("the price has been change")
                             i=0
                        if (i):
                             print("there is no product has this id")
                       
                case 5:
                        found=False
                        SearchedProduct=input("Enter product ID to delete")
                    
                        for product in Library.products:
               
                          if (str(product.product_id)==SearchedProduct):
       
                               Library.products.remove(product)
                               print("the price has been deleted")
                               found=True
                          if (not found):
                               print("there is no product has this id")
                case 6:
                     SearchedProduct=input("Enter product ID to Change status")
                     found=False
                     for product in Library.products:

                          
                          if (str(product.product_id)==SearchedProduct):

                               status=int(input("Enter the new status"))
                               product.change_status(status)
                               print("the status has been change  ")
                               found=True
                     if (not found):
                      print("there is no product has this id")
                case 7:
                    os.system("cls")
                    main_project()            
                    break
                case _:print("out of the scope,please try againe:")
            print("----------------------------\n")
            PrintProductMenu()
            choice=int(input("enter another choice:"))
            


    def  category_process():
        
        while True:
            PrintCategoryMenu()
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    Library.AddCategory()
                case 3:
                    Library.DisplayProductByCategory()
                case 2:
                    Library.Display
                case 4:pass
                  
                case _:
                    print("Invalid choice.")
                
        
    def employee_process():

        

        while True:
            PrintEmployeeMenu()
            choice=int(input("enter your choice:"))
            match choice:
                case 1:
                   i ='y'
                   while(i=='y' or i== 'Y'):
                     os.system("cls")
                     info =create_employee()
                   # info =[ employee_id, name, jobs, phone, salary]
                     Library.AddEmployee(info[0],info[1],info[3], info[4],info[2])
                     print("employee Created .")
                     i=input("do you wante to enter another Employee Y/N")
                   
                   os.system("cls")
                   PrintEmployeeMenu()
                #make visulse for add Employee #$bashar  
                case 2:
                   os.system("cls")
                   PrintEmployeeDisplayHeader(Library.Employees)
                
                case 3:
                    os.system("cls")
                    Library.SearchEmployee()
                case 4:
                    employeeid=int(input("enter the employee id:"))
                    found=False
                    for Employees in Library.Employees:
                       
                       if Employees.employee_id==employeeid:
                            new_salary=int(input("enter the new salary:"))
                            Employees.update_salary(new_salary)
                            
                            found=True
                    if (not found):
                      print("There is no Employee has this id")
                        
                case 5:
                    SearchedProduct=input("Enter Employee ID to delete")
                    found=False
                    for Employee in Library.Employees:
               
                          if (str(Employee.employee_id==SearchedProduct)):
       
                               Library.Employees.remove(Employee)
                               print("the Employee has been deleted")
                               found=True
                    if (not found):
                         print("there is no Employee has this id")
                
                case 6:
                    os.system("cls")
                    print("========================\n \n")
                    print(f"the number of employees is: ",len(Library.Employees))
                    print("--------------------\n \n ")
                case 7:
                    os.system("cls")
                    main_project()
                    break
                case _:
                    print("out of the scope,please try againe:")
                    print("----------------------------\n")
                    choice=int(input("enter another choice:"))

                
    
    def Report_process():
        

        while True:
            PrintReportsMenu()
            choice=int(input("Eenter your choice:"))
            match choice:
                case 1:
                    os.system("cls")
                    print("================Porduct Report==================")
                    print(f"Total Product: {len(Library.products)}\n")
                    print("Avlible product :")
                    
                    for pro in Library.products:
                        if(str(pro.status)=='1'):
                            print(f"-{pro.name}")

                    print("=================================================")
                case 2:
                    os.system("cls")
                    print("================Porduct Report==================")
                    print(f"Total Employee: {len(Library.Employees)}\n")
                    print("Empoyee list :\n")
                    print(f" {'Name' :<20}{'Role' :<15}")
                    for pro in Library.Employees:
                        
                         print(f" {pro.name :<20}{pro.jobs :<15}")

                    print("=================================================")
                case 3:
                    os.system("cls")
                    print("-------------------------")
                    print("the section is not completed")
                    print("-------------------------")
                    
                case 4:
                    os.system("cls")
                    main_project()
                    break
                case _:print("out of the scope,please try againe:")
    

    def main_project():
        
        
        PrintMainMenu()
    
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                os.system("cls")
                products_process()
            case 2:
                os.system("cls")
                category_process()
            case 3:
                os.system("cls")
                employee_process()
            case 4:
                os.system("cls")
                PrintSalesMenu()
            case 5:
                os.system("cls")
                Report_process()
            case 6:
                SaveEmployee(Library.Employees)
                SaveProduct(Library.products)
                SaveSalas(Library.sales)
                os.system("cls")
                print("Goodbye!")
            case _:
                print("Invalid choice. Please try again.")


           

           
        
    
    PrintWelcomeMassage()    
    main_project()            
         


if __name__ == "__main__":
    main()


    

