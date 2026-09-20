# from product import Product
# class Inventory:
#     counter=1
#     def __init__(self,inventory_id, products_stock):
#         self.inventory_id=Inventory.counter
#         Inventory.counter+=1
#         self.products_stock=products_stock

#     def add_stock(self,product, quantity):
#         if product in self.products_stock:
#             self.products_stock[product]+=quantity
#         else:
#             self.products_stock[product]=quantity
#             # self.products_stock[product] = self.products_stock.get(product, 0) + quantity

#     def remove_stock(self, product, quantity):
#         if product in self.products_stock:
#             if self.products_stock[product]>=quantity:
#                 self.products_stock[product] -= quantity
#             else:
#                 print("Not enough stock")
#         else:
#             print("Product not found")
#     def check_stock(self, product):
#         if product in self.products_stock:
#             return self.products_stock[product]
#         else:
#             return 0
#     def inventory_report(self):
#         for product, quantity in self.products_stock.items():
#             print("Product:", product)
#             print("Quantity:", quantity)