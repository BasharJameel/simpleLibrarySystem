from utils.display import PrintWelcomeMassage, PrintMainMenu, PrintProductMenu, PrintCategoryMenu, PrintEmployeeMenu, PrintInventoryMenu, PrintSalesMenu, PrintReportsMenu
from models.store import store

def main():
    PrintWelcomeMassage()
    
    Library = store("bashar store")
    
    
    PrintMainMenu()
    
    choice = int(input("Enter Your Choice: "))
    
           
           
        
    match choice:
            case 1:
                PrintProductMenu()
            case 2:
                PrintCategoryMenu()
            case 3:
                PrintEmployeeMenu()
            case 4:
                PrintInventoryMenu()
            case 5:
                PrintSalesMenu()
            case 6:
                PrintReportsMenu()
            case 7:
                print("Goodbye!")
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


    

