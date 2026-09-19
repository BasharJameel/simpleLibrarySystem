from utils.display import PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintInventoryMenu, PrintSalesMenu, PrintReportsMenu
from models.store import *
from utils.helpers import *
from GUI.CreateAnewProducteInterface import *
import os
def main():
    #ask to enter the name of employee and check from file of employee 
    #store it in متغير to add it in saleitem and sale
    
    Library=Store("basharstore")

    LoadProduct(Library)
    
    
    
        
    def products_process():

        PrintProductMenu()
        
        choice=int(input("enter your choice:"))
        while True:
            
            match choice:
                case 1:AddProductGUI()

                       
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
                    pass
                    break
                case 6:
                    pass
                    break
                case 7:
                    main_project()            
                    break
                case _:print("out of the scope,please try againe:")
            print("----------------------------\n")
            choice=int(input("enter another choice:"))
            




    def  category_process():
        PrintCategoryMenu()
        while True:
            choice = int(input("Enter Your Choice: "))
            match choice:
                case 1:
                    pass
                    break
                case 2:
                    pass
                    break
                case 3:
                    main_project()
                    break
                case _:print("Invalid choice. Please try again.")
                
        

    
    def employee_process():

        PrintEmployeeMenu()
        while True:
            choice=int(input("enter your choice:"))
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
                    pass
                    break
                case 6:
                    pass
                    break
                case 7:
                    os.system("cls")
                    main_project()
                    break
                case _:print("out of the scope,please try againe:")




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
                category_process()
            case 3:
                employee_process()
            case 4:
                inventory_process()
            case 5:
                PrintSalesMenu()
            case 6:
                PrintReportsMenu()
            case 7:
                print("Goodbye!")
            case _:
                print("Invalid choice. Please try again.")
           
           
        
    
    PrintWelcomeMassage()    
    main_project()            
         

    

    

if __name__ == "__main__":
    main()


    

