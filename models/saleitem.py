class saleitem:
    def __init__(self,product,quantity,subtotal=0): 
        self.product=product
        self.quantity=quantity
        self.subtotal=subtotal

    # def  calculate_subtotal(self):
    #     self.subtotal=self.quantity*self.price_unit
    #     return self.subtotal

    def display_item(self,porudts):
        for product in porudts:
            if str(self.product)==str(product.product_id):
              print(f"product:{product.name} |quantity:{self.quantity} " )
 


