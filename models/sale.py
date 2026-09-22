from models.product import Product
from models.saleitem import saleitem
from models.payment import payment

from datetime import date
class sale:
    counter=1
    def __init__(self,employee,payment,items,total):
        self.sale_id=sale.counter
        sale.counter+=1
        self.date=date.today()
        self.employee=employee#add the متغير from main ||||this must be a obj
        self.total=total
        self.items=items
        self.payment=payment

          #%***% is Ammar make this a objct

    
    def add_item(self,item):
        self.items.append(item)

    def item_remove(self,id_item):
            
            if id_item>0 and id_item<=len(self.items):
                self.items.pop(id_item-1)
                print("the  remove is successfully")
                
            else:
                print("error item")

    # def calculate_total(self):
    #     self.total=0
    #     for item in self.items:
    #         total+=item.calculate_subtotal()
    #     return total
    

    def display_sale(self,employee,product):

        print("\n \n =========================")
        print(f"sale_id:{self.sale_id}")
        print(f"date:{self.date}")
        print(f"employee: {self.employee}")
        print("---------------------------------------------")
        for  item in self.items :        
               item.display_item(product)
        print("__________________________________________")
        print(f"total  of sale:{self.total}")

        print("$$$$$$$$$$$$$$..PAYMENT..$$$$$$$$$$$$$$$$$$")
        print(f"           {self.payment.display_payment()}")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        

def calcalutSubitem(id ,quantity,productsList):
    for product in productsList:
        if str(product.product_id)==str(id):
            return product.price*quantity
        



def create_saleitem(productsList):
    listItems=[]  
    while True:
        product_id=input("enter the product id:\n")#we can develop this part by make the parmete is OBj
        quantity=int(input("enter the quantity\n"))

        # total_item=saleitem.calculate_subtotal()
        # item =saleitem(product_id,quantity,total_item)
        # self.add_item(item)
        subitem_total=calcalutSubitem(product_id,quantity,productsList)
        listItems.append(saleitem(product_id, quantity,subitem_total))
        repeat=input("do you want to add another item Y/N:")
        if repeat=="y" or repeat=="Y":
            continue
        else:
            break
    return listItems

def calculate_total(items):
        total=0
        for item in items:
            print("subtotal=",item.subtotal)
            total+=item.subtotal
        return total



  