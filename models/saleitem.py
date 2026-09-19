class saleitem:
    def __init__(self,product,quantity,price_unit=0,subtotal=0): 
        self.product=product
        self.quantity=quantity
        self.price_unit=price_unit
        self.subtotal=subtotal

    def  calculate_subtotal(self):
        self.subtotal=self.quantity*self.price_unit
        return self.subtotal

    def display_item(self):
        print(f"product:{self.product}" )
        print(f" quantity:{self.quantity} ")
        print(f"price: {self.price_unit} ")
        print("===============total price=================")
        print(f"total price: {self.calculate_subtotal()}")
        print("===============total price=================")



