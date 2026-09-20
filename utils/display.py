import os
def PrintWelcomeMassage ():
    print("=====================================")
    print("       Store Mangement System")
    print("=====================================")
    print("Welcome to Store Mangement System :-)\n")

    input(" Press Enter to continue")
    os.system("cls")


def PrintMainMenu():
    print("=====================================")
    print("             Main Menu               ")
    print("=====================================")
    print("1. Products")
    print("2. Categories")
    print("3. Employee")
    print("4. Sales")
    print("5. Reports")
    print("6. Exit")
    


def PrintProductMenu():
    print("=====================================")
    print("           Product Menu              ")
    print("=====================================")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Product Price")
    print("5. Delete Product")
    print("6. Change Product Status")
    print("7. Back")


def PrintCategoryMenu():
    print("=====================================")
    print("          Category Menu              ")
    print("=====================================")
    print("1. Add Categories")
    print("2. Display Categories")
    print("3. Display Products by Category")
    print("4. Back")


def PrintEmployeeMenu():
    print("=====================================")
    print("          Employee Menu              ")
    print("=====================================")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Employee Count")
    print("7. Back")



def PrintSalesMenu():
    print("=====================================")
    print("            Sales Menu               ")
    print("=====================================")
    print("1. New Sale")
    print("2. Display Sales")
    print("3. Search Sale")
    print("4. Back")


def PrintReportsMenu():
    print("=====================================")
    print("           Reports Menu              ")
    print("=====================================")
    print("1. Products Report")
    print("2. Employees Report")
    print("3. Sales Report")
    print("4. Back")


def PrintEmployeeTypeMenu():
    print("=====================================")
    print("         Employee Type               ")
    print("=====================================")
    print("1. Manager")
    print("2. Cashier")
    print("3. Storekeeper")
    print("4. Back")


def PrintPaymentMenu():
    print("=====================================")
    print("           Payment Method            ")
    print("=====================================")
    print("1. Cash")
    print("2. Card")
    print("3. Back")

def PrintEmployeeDisplayHeader(Employees):
    
    
    print("=====================================")
    print("     Employees List             ")
    print("=====================================")
    for Employee in Employees:
        print(F"-{Employee.name}")


def PrintGoodbye():
    print("=====================================")
    print("     Thank You, Goodbye!             ")
    print("=====================================")