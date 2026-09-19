class Product:
    counter=1
    def __init__(self,product_id , name , price, category,description , status ):
        self.product_id=Product.counter
        Product.counter+=1
        self.name= name 
        self.price = price
        self.category=category
        self.description=description
        self.status=status

    @property
    def price(self):
        # Private تجعل المتغير
        # product.price
        #    ↓
        # @property
        #    ↓  
        # __price

        # فائده عمل __price
        # ا نسمح بالتعامل معه مباشرة، بل نستخدم 
        return self.__price
    
    # هذا يتحكم في تغيير السعر
    @price.setter
    def price(self, price):
        if Product.is_valid_price(price):
            self.__price = price
        else:
            self.__price = 0
#    هذه دالة لا تحتاج Object معين لكي تعمل.
    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False
        
    def update_price(self, new_price):
        
        self.price = new_price

    def change_status(self, new_status):
        self.status = new_status

    def is_available(self):
        if self.status == "Available":
            return True
        else:
            return False

    # display_info()      → عرض معلومات المنتج
    # update_price()      → تحديث السعر
    # change_status()     → تغيير الحالة
    # is_available()      → التحقق من توفر المنتج
    # is_valid_price()    → التحقق من صحة السعر
    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Description:", self.description)
        print("Category:", self.category)
        print("Status:", self.status)
