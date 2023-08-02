import pandas as pd
from datetime import date
import csv

def main():
    print("<----- 彡 W E L C O M E  M Y S H O P 彡----->\n")
    print("Who are you?\n1.User\n2.Manager")
    print()
    sec = int(input("Select: ")) 
    if(sec==1):
        User()
    elif(sec==2):
        Manager()
    else: 
        main()
     
def User():
    print("1.View Product\n2.Purchase Product\n3.Cancle Order\n")
    sec = int(input("Select: "))
    if(sec==1):
        View_Products()
    elif(sec==2):
       Purchase_Product() 
    elif(sec==3):
        Cancle_Order()
    else:
        print("Wrong Seletion!!!")
        User()
def View_Products():
    print("\n  Display All Product\n=======================")
    loc = r'E:\Code\Python\product.csv'
    with open(loc,'r') as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print("<----------------->")
        for i in cd.index:
            x = list(cd.loc[i])
            print("PID: ",i)
            print("Name: ",x[0])
            print("Cost: ",x[1])
            print("Brand: ",x[2])
            print("<----------------->")
        cf.close()
        print("\nWhat do you want to do?")
        cho = int(input("1.Go to User Section\n2.Exit\nChoise: "))
        if(cho==1):
            User()
        elif(cho==2):
            exit()
        else:
            print("Wrong Selection!!!")
            exit()
       
def Cancle_Order():
    loc = r'E:\Code\Python\order.csv'
    pro_id = input("Product Id: ")
    quan = int(input("Quantity: "))
    name = input("Name: ")
    address = input("Address: ")
    da = input("Date: ")
    row = [name,address,da,pro_id,quan]
    with open(loc,'r+') as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        for i in cd.index:
            x = list(cd.loc[i])
            if(row==x):
                cd.drop([i],inplace=True)
    cf.close()
    
    with open(loc,'w',newline="") as cf:
        cw = csv.writer(cf)
        for i in cd.index:
            x = list(cd.loc[i])
            cw.writerow(x)
    cf.close()
    print("\nWhat do you want to do?")
    cho = int(input("1.Go to User Section\n2.Exit\nChoise: "))
    if(cho==1):
        User()
    elif(cho==2):
        exit()
    else:
        print("Wrong Selection!!!")
        exit()
            
      
def Purchase_Product():
    
    loc = r'E:\Code\Python\order.csv'
    pro_id = input("Product Id: ")
    quan = int(input("Quantity: "))
    name = input("Name: ")
    address = input("Address: ")
    da = date.today()
    row = [name,address,da,pro_id,quan]
    with open(loc,'a+',newline="") as cf:
        cw = csv.writer(cf)
        cw.writerow(row)
    cf.close()
    print("\nWhat do you want to do?")
    cho = int(input("1.Go to User Section\n2.Exit\nChoise: "))
    if(cho==1):
        User()
    elif(cho==2):
        exit()
    else:
        print("Wrong Selection!!!")
        exit()
    
                
'''   
print("Are you sure to buy this product?")
    con = int(input("1.Yes\n2.No\n"))
    if(con==1):
        print("Ok Sir...\n")
        loc = r'E:\Code\Python\product.csv'
        
        with open(loc,'r+') as cf:
            cw = csv.reader(cf)
            cd = pd.DataFrame(cw)
            for i in cd.index:
                x = list(cd.loc[i])
                if(row==x):
                    tk = x[1] * quan
                    print("Which Way you pay your bill\n1.Card\2.Cash\n")
                    sec = int(input("Select: "))
                    if(sec==1):
                        print("Your bill",tk)
                        pay =int(input("Pay: "))
                        if(pay>tk):
                            print("Thank You sir.")
                            print("Refound: {} taka".format(pay-tk))
                        elif(pay==tk):
                            print("Thank You sir.")  
                    else:
                        print("Product Not Available")
      
            cf.close()     
         
        elif(con==2):
            Purchase_Product()
        else:
            print("Wrong Selection.")

    print("\nWhat do you want to do?")
    cho = int(input("1.Go to User Section\n2.Exit\nChoise: "))
    if(cho==1):
        User()
    elif(cho==2):
        exit()
    else:
        print("Wrong Selection!!!")
        exit()
   
    
    '''

    
def Manager():
    global cou
    pas = int(input("Enter Password: "))
    if(pas==123):
        print("Successfully loging!!!\n")
        print("What do you want to do?")
        print("1.Add Product\n2.View Product\n3.Delet Product\n4.Check Order\n5.Exit\n")
   
        sec = int(input("Select: "))
        if(sec==1):
            Add_Product()
        elif(sec==2):
            View_Product()
        elif(sec==3):
            Delect_Prodcuct()
        elif(sec==4):
            Check_Order()
        elif(sec==5):
            exit()
        else:
            Manager()
    else:
        cou=cou+1
        if(cou<2):
            print("Wrong Password!Try again")
            Manager()
        else:
            print("Sorry Sir!Your Password Wrong\nStarting to the Initial Stage...")
            main()
            
def Add_Product():
    name = input("Name: ")
    cost = input("Cost: ")
    Brand = input("Brand: ")
    row = [name,cost,Brand]
    
    loc = r'E:\Code\Python\product.csv'
    with open(loc,'a+',newline="") as cf:
        cw = csv.writer(cf)
        cw.writerow(row)
    cf.close()
    print("What do you want to do?")
    cho = int(input("1.Go to Manager Section\n2.Go to User Section\n3.Exit\nChoise: "))
    if(cho==1):
        Manager()
    elif(cho==2):
        User()
    elif(cho==3):
        exit()    

def View_Product():
    print("\n  Display All Product\n=======================")
    loc = r'E:\Code\Python\product.csv'
    with open(loc,'r') as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print("<----------------->")
        for i in cd.index:
            x = list(cd.loc[i])
            print("PID: ",i)
            print("Name: ",x[0])
            print("Cost: ",x[1])
            print("Brand: ",x[2])
            print("<----------------->")
        cf.close()
        print("\nWhat do you want to do?")
        cho = int(input("1.Go to Manager Section\n2.Go to User Section\n3.Exit\n\nChoise: "))
        if(cho==1):
            Manager()
        elif(cho==2):
            User()
        elif(cho==3):
            exit()
        
     
def Delect_Prodcuct():
    id = int(input("Product ID: "))
    loc = r'E:\Code\Python\product.csv'
    with open(loc,'r+') as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        cd.drop([id],inplace=True)
        cf.close()
        with open(loc,'w',newline="") as cf:
            cw = csv.writer(cf)
            for i in cd.index:
                x = list(cd.loc[i])
                cw.writerow(x)
    cf.close()
    print("\nWhat do you want to do?")
    cho = int(input("1.Go to Manager Section\n2.Go to User Section\n3.Exit\n\nChoise: "))
    if(cho==1):
        Manager()
    elif(cho==2):
        User()
    elif(cho==3):
        exit()       
        
        
        
def Check_Order():
    print("----- Number of Customers Purchase List -----\n")
    loc = r'E:\Code\Python\order.csv'
    with open(loc,'r') as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print("----------------------------------------------------------")
        for i in cd.index:
            x = list(cd.loc[i])
            print("Name:{}  Address:{}  Date:{}  PID:{}  Quantity: {}".format(x[0],x[1],x[2],x[3],x[4]))
            print("----------------------------------------------------------")
            
        cf.close()
        print("\nWhat do you want to do?")
        cho = int(input("1.Go to Manager Section\n2.Go to User Section\n3.Exit\n\nChoise: "))
        if(cho==1):
            Manager()
        elif(cho==2):
            User()
        elif(cho==3):
            exit()
        
cou=0
main()