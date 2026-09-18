from datetime import date
class payment:
    counter=192168
    def __init__(self,amount,method):
        self.payment_id=payment.counter
        payment.counter+=10
        self.amount=amount
        self.method=method
        self.date=date.today()


    def  process_payment(self,total):
        
        
        self.amount=int(input("enter the monay the customer give:"))
           
        if self.amount<total:
            still=total-self.amount
            print(f"......astill have :{still}")
            astill1=int(input("..........how mutch does he give you:"))
            if astill1==still:
                    print("............DONE")
        elif self.amount>total:
            print(f"you must to give them {self.amount-total}")
            

        else:
            print("DONE")


            self.method=input("enter the way the customer give you the mony:")

            print(f"amount:{self.total}")
            print(f"method:{self.method}")



    def display_payment(self):
        print(f"payment_id:{self.payment_id}")
        print(f"amount:{self.amount}")
        print(f"method{self.method}")
        print(f"date:{self.date}")
        


                




        