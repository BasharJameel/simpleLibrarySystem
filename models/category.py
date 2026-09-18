class Category:
    counter=1
    def __init__(self,category_id,name,description):
        self.category_id=Category.counter
        Category.counter+=1
        self.name=name
        self.description=description
        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def count_products(self):
        return len(self.products)
    
    def display_info(self):
        print("Category ID: ",self.category_id)
        print("Category Name: ",self.name)
        print("Category description: ",self.description)
        print("Category products: ",self.products)
