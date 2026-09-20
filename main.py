from utils.display import PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintInventoryMenu, PrintSalesMenu, PrintReportsMenu
from utils.display import PrintEmployeeDisplayHeader, PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintInventoryMenu, PrintSalesMenu, PrintReportsMenu
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
                    while(i=="Y"):

                     os.system("cls")
                     Library.SearchProduct()
                     i=input("Do you wante to enter search agine Y/N")
                case 4:
                    pass
                    break#creat  update interface
                case 5:
                    pass
                    #Creat menu to delet prodct 
                case 6:
                    pass
                    #Creat a interface of change stats
                    break
                case 7:
                    os.system("cls")
                    main_project()            
                    break
                case _:print("out of the scope,please try againe:")
            print("----------------------------\n")
            PrintProductMenu()
            choice=int(input("enter another choice:"))
            




    def  category_process():
        PrintCategoryMenu()
        while True:
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    pass
                    #creat interface call the list  of category and print it
                    break
                case 2:
                    pass
                    break
                    #I make it in the in store.py (DisplayProduct - line 44) 
                case 3:
                    os.system("cls")
                    main_project()
                    break
                case _:print("Invalid choice. Please try again.")
                
        

    
    def employee_process():

        PrintEmployeeMenu()

        while True:
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
                   PrintEmployeeDisplayHeader(Library.Employees)
                   break
                
                case 3:
                    os.system("cls")
                    Library.SearchEmployee()
                case 4:
                    
                    for Employees in Library.Employees:
                       employeeid=int(input("enter the employee id:"))
                       if Employees.employee_id==employeeid:
                            new_salary=int(input("enter the new salary:"))
                            Employees.update_salary(new_salary)
                    else:
                        print("error id")
                        
                case 5:
                    pass
                    break
                case 6:
                    os.system("cls")
                    print(f"the number of employees is: ",len(Library.Employees))
                case 7:
                    os.system("cls")
                    main_project()
                    break
                case _:
                    print("out of the scope,please try againe:")
                    print("----------------------------\n")
                    choice=int(input("enter another choice:"))




    def inventory_process():
        
        PrintInventoryMenu()
        while True:
            choice=int(input("Eenter your choice:"))
            match choice:
                case 1:
                    pass
                    break
                case 2:
                    pass
                    break
                case 3:
                    pass
                    break
                case 4:
                    pass
                    break
                case 5:
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
                inventory_process()
            case 5:
                os.system("cls")
                PrintSalesMenu()
            case 6:
                os.system("cls")
                PrintReportsMenu()
            case 7:
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


    

