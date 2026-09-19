from product import Product
from models.saleitem import saleitem
from datetime import date
class sale:
    counter=1
    def __init__(self,employee,payment):
        self.sale_id=sale.counter
        sale.counter+=1
        self.date=date.today()
        self.employee=employee#add the متغير from main 
        self.total=0
        self.items=[]
        self.payment=payment

    
    def add_item(self,item):
        self.items.append(item)

    def item_remove(self,id_item):
            
            if id_item>0 and id_item<=len(self.items):
                self.items.pop(id_item-1)
                print("the  remove is successfully")
                
            else:
                print("error item")

    def calculate_total(self):
        self.total=0
        for item in self.items:
            self.total+=item.calculate_subtotal()
        return self.total
    

    def display_sale(self):
        print(f"sale_id:{self.sale_id}")
        print(f"date:{self.date}")
        print(f"employee:")#enter the name of employee from main
        print("---------------------------------------------")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. ", end="")
            item.display_item()

        print(f"total  of sale:{self.calculate_total()}")
        
        

    def create_saleitem(self):
        while True:
            product_id=input("enter the product id:\n")
            quantity=int(input("enter the quantity\n"))
            
            price_unit=float(input("enter the price perice unit:\n"))
            total_item=saleitem.calculate_subtotal()
            item =saleitem(product_id,quantity,price_unit,total_item)
            self.add_item(item)

            repeat=input("do you want to add another item:")
            if repeat=="yes" or repeat=="Yes":
                continue
            else:
                break



  