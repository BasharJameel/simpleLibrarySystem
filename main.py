from utils  import display
from models.store import store


display.PrintWelcomeMassage()
display.PrintMainMenu()
choice =int(input("Enter Your Choice"))

Library=store("bashar store")

match choice:
    case 1:display.PrintProductMenu()
    case 2:display.PrintCategoryMenu()
    case 3:display.PrintEmployeeMenu()
    case 4:display.PrintInventoryMenu()
    case 5:display.PrintSalesMenu()
    case 6:display.PrintReportsMenu()
    case 7:print("is not complete yet")


def ProductMenu():
    display

