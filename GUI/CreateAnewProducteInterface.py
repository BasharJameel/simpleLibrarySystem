import tkinter as tk


def AddProductGUI():

    def SaveProduct():
        id=idText.get()
        name=nameText.get()
        price=PriceText.get()
        Catgories=CatgoriesText.get()
        Description=DescriptionText.get()
        Status=StatusText.get()



        idText.delete(0, tk.END)
        nameText.delete(0, tk.END)
        PriceText.delete(0, tk.END)
        CatgoriesText.delete(0, tk.END)
        DescriptionText.delete(0, tk.END)
        StatusText.delete(0, tk.END)

    root=tk.Tk()
    root.geometry("800x500")
    root.title("librarySystem/a New Product")

    Lable=tk.Label(root, text= "insert the new product", font= "Tahoma 16 bold ")
    Lable.grid(row=0, column=0,columnspan=5, padx=10, pady=20)

    idLable=tk.Label(root, text= "ID", font= "Tahoma 12 bold ")
    idLable.grid(row=1, column=0, padx=5 , pady=25)
    
    idText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    idText.grid(row=1, column=1, padx=(0,100), pady=10)

    nameLable=tk.Label(root, text= "name", font= "Tahoma 12 bold ")
    nameLable.grid(row=1, column=2, padx=(5,0), pady=10)

    nameText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    nameText.grid(row=1, column=3, padx=(0,5), pady=10)





    pricelable=tk.Label(root, text= "Price", font= "Tahoma 12 bold ")
    pricelable.grid(row=2, column=0, padx=5 , pady=25)
    
    PriceText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    PriceText.grid(row=2, column=1, padx=(0,100), pady=10)

    CatgoriesLable=tk.Label(root, text= "Catgories", font= "Tahoma 12 bold ")
    CatgoriesLable.grid(row=2, column=2, padx=(5,0), pady=10)

    CatgoriesText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    CatgoriesText.grid(row=2, column=3, padx=(0,5), pady=10)


    Descriptionlable=tk.Label(root, text= "Description", font= "Tahoma 12 bold ")
    Descriptionlable.grid(row=3, column=0, padx=5 , pady=25)
    
    DescriptionText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    DescriptionText.grid(row=3, column=1, padx=(0,100), pady=10)

    StatusLable=tk.Label(root, text= "Status", font= "Tahoma 12 bold ")
    StatusLable.grid(row=3, column=2, padx=(5,0), pady=10)

    StatusText=tk.Entry(root,bg="gray",width=20,font="Tahoma 12 bold")
    StatusText.grid(row=3, column=3, padx=(0,5), pady=10)




    SaveButton= tk.Button(root, text="save", width=10,height=1,command=SaveProduct)
    SaveButton.grid(row=4, column=0,columnspan=5,pady=50)




    


    root.mainloop()



