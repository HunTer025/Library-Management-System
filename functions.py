
def functions():
    
    def dictionary_books():
        file = open("books.txt","r")
        dictionarybooks={}
        bookID = 0
        for line in file:
            bookID = bookID+1
            line = line.replace("$","")
            line = line.replace("\n","")
            dictionarybooks[bookID] = line.split(",")
            
        file.close()
        return dictionarybooks



    def dictionary_write():
        file = open("books.txt","w")
        for values in dictB.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
                    
        file.close()

    def bill():
        import datetime
        second = str(datetime.datetime.now().second)
        micro = str(datetime.datetime.now().microsecond)
        random= second + micro
        file = open("Borrow_"+name+"("+random+")"+".txt","w")
        file.write("Name of the customer:"+str(name))
        file.write("\nThe total sum of price: $"+str(sumPrice))
        file.write("\nDate and time of books borrowed:"+str(random))
        for i in range(len(book)):
            file.write("\n Borrowed books are:"+str(book[i]))
        file.close()
        
    def r_write():
        import datetime
        second = str(datetime.datetime.now().second)
        micro = str(datetime.datetime.now().microsecond)
        random= second + micro
        file = open("Return_"+name+"("+random+")"+".txt","w")
        file.write("Name of the returner:"+str(name))
        file.write("\nFine added for exceeding date(per day $0.1): $"+str(totalfine))
        file.write("\nDate and time of books returned:"+str(random))
        for i in range(len(book)):
            file.write("\n Returned books are:"+str(book[i]))
        file.close()
        
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
              "\t\t Hello and welcome to my library management \n"
              "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    def file_open():    
        print("--------------------------------------------------------------------------------")
        print("Book ID " + " Book-Name \t"  + " Author \t" + "Quantity   " + "Price($)" )
        print("--------------------------------------------------------------------------------")
        dictionary ={}
        file = open("books.txt","r")
        bookID = 0

        for line in file:
            bookID = bookID + 1
            line = line.replace("$","")
            line = line.replace("\n","")
            dictionary [bookID] = line.split(',')
            line = line.replace(",", " \t")
            
            print(bookID, "\t", line)
        
        print("\n--------------------------------------------------------------------------------\n")
        
        file.close()
           
    
    correctInput = False

    while correctInput == False:
            
        try:
            loop = True
            while loop == True:
                file_open()
                print("Enter 1 to borrow a book")
                print("Enter 2 to return a book")
                print("Enter 3 to exit")

                val = int(input("Please enter a value:"))
                
                if val == 1:
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                          "\t\tYou will now borrow book!!\n"
                          "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
                    price=[]
                    book=[]

                    Bloop = True

                    while Bloop == True:
                        
                        bookID = int(input("Enter the ID of the book:"))
                        dictB = dictionary_books()
                                    
                        while bookID<=0 or bookID>len(dictB):
                            bookID= int(input("Enter the ID of the book: "))
                        if(int(dictB[bookID][2])) == 0:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                    "\t\t Book is not available!!\n"
                                    "+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            
                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                    "\t\t Book is available!!\n"
                                    "+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            Bloop=False
                            
                            name = input("Enter the name of the borrower:")
                            price.append(dictB[bookID][3])
                            
                            book.append(dictB[bookID][0])
                            print("The price of the book is $",(dictB[bookID][3]))
                            import datetime
                            datetime = str(datetime.datetime.now())
                            
                            print("Date and time of borrow is ",datetime)
                            total = list(map(float,price))
                            sumPrice = sum(total)
                            
                            (dictB[bookID][2])= int((dictB[bookID][2]))-1
                                
                               
                            dictionary_write()
                            
                            print("\n"
                                "Library after borrow is: ")
                            file_open()
                            
                            Aloop = True
                            while Aloop == True:
                                another=input("Would you like to borrow another book as well?\n"
                                                "If 'Yes' please enter 'Y' or else provide any other value:")
                                if another == "Y" or another == "y":

                                    bookID = int(input("Enter the ID of the book:"))
                                    
                                    while bookID<=0 or bookID>len(dictB):
                                        bookID= int(input("Enter the ID of the book: "))
                                        
                                    if(int(dictB[bookID][2]))==0:
                    
                                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                            "\t\t Book is not available!!\n"
                                            "+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                                        print("\n")
                                        print ("Name of the customer: ",name)
                                        print ("Total price : ","$",sumPrice)
                                        print ("Date and time of borrow: ", datetime)
                                        print ("Books borrowed are: ")
                                        for i in range(len(book)):
                                            print(book[i])
                                        break
                                    else:
                                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                                "\t\t Book is available!!\n"
                                                "+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                                        price.append(dictB[bookID][3])
                                        book.append(dictB[bookID][0])
                                        total = list(map(float,price))
                                        sumPrice = sum(total)
                                        dictB[bookID][2] = int(dictB[bookID][2]) - 1
                                        dictionary_write()
                                        print("\n"
                                            "Library after borrow is: ")
                                        file_open()
                                        
                                else:
                                    Aloop = False
                                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                          "\t\t Customer Borrow Details\n"
                                          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    
                                    print("Name of the customer:",name)
                                    print("Total price from borrow:","$",sumPrice)
                                    print("Date and time of borrow:",datetime)
                                    print("Books borrowed are:")
                                    for i in range(len(book)):
                                        print(book[i])
                                    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    bill()
                                    
                                    
                                    
                
                if val == 2:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                          "\t\tYou will now return the book!!\n"
                          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
                    name = input("Enter the name of the borrower:")
                    book=[]
                    Cloop = True

                    while Cloop == True:
                        
                        bookID = int(input("Enter the ID of the book you want to return:"))
                        dictB = dictionary_books()
                                        
                        while bookID<=0 or bookID>len(dictB):
                            bookID= int(input("Enter the ID of the book you want to return: "))
                        if bookID == 1 or bookID == 2 or bookID == 3 or bookID == 4 or bookID == 5:
                            print("\n"
                                    "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                      "\t \t Book is returned!!\n"
                                         "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            book.append(dictB[bookID][0])
                            
                            dictB[bookID][2] = int(dictB[bookID][2]) + 1
                            import datetime
                            datetime = datetime.datetime.now()
                            
                            dictionary_write()
                            print("\n"
                                    "Library after return of book is: ")
                            file_open()

                            Cloop = False
                        else:
                            
                            print("++++++++++++++++++++++++++++++++++++++++++++\n"
                                    "\t\tPlease provide a valid Book ID!!\n"
                                    "++++++++++++++++++++++++++++++++++++++++++++")
                            
                    Dloop = True
                    while Dloop == True:
                        
                        another=input("Have this person borrowed another book as well?\n"
                                        "If 'Yes' please enter 'Y' or else provide any other value:")
                        if another == "Y" or another == "y":

                            bookID = int(input("Enter the ID of the book:"))
                            
                            while bookID<=0 or bookID>len(dictB):
                                bookID= int(input("Enter the ID of the book: "))
                            if bookID == 1 or bookID == 2 or bookID == 3 or bookID == 4 or bookID == 5:
                                print("\n"
                                        "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                          "\t \t Book is returned!!\n"
                                             "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    
                                dictB[bookID][2] = int(dictB[bookID][2]) + 1

                                dictionary_write()
                                file_open()

                            else:
                                print("\n"
                                        "Library after return of book is: ")
                            
                                file_open()
                        else:
                            try:
                                fine = int(input("Enter the number of days you have borrowed the book:"))
                            except:
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                      "\t\tPlease enter an integer value!!!!\n"
                                      "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                
                            fineamt = 0
                            finelist=[]
                            if fine > 10:
                                fineamt = (fine - 10)*0.10
                                finelist.append(fineamt)
                                totalfine = sum(finelist)
                                
                            else:
                                totalfine=0
                                
                            Dloop = False
                            book.append(dictB[bookID][0])
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                          "\t\t Customer return Details\n"
                                          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    
                            print("Name of the customer:",name)
                            print("Fine added for exceeding date(per day $0.1): $",totalfine)
                            print("Date and time of return:",datetime)
                            print("Books returned are:")
                            for i in range(len(book)):
                                print(book[i])
                            print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            r_write()
                            
                            
                if val == 3:
                    loop = False
                
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                        "\t\tThank you For using our Library management system\n"
                          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")     
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                          "\t\tPlease provide value as 1, 2 or 3!!!\n"
                          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
            correctInput =True
            break
        except:
            
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                "\t\tplease enter a valid input!!\n"
                  "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
functions()



