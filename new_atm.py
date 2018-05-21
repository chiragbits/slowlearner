userName=('chirag mittal','anurag mittal')
password=[1993,1994]
balance=[1000,2000]
user_name=input("ENTER USERNAME: ")
pass_word=int(input("ENTER YOUR PASSWORD: "))
for ind in range(0,len(userName),1):
    if(user_name==userName[ind] and pass_word==password[ind]):
        print("credentials matching")
        
        print("PLEASE ENTER THE FOLLOWING ONE OPTION:\n1. withdraw\n2. deposit\n3. account statement\n4. quit")
        options=int(input("enter the options 1/2/3/4: "))
        if(options==1):
            amount_withdraw=int(input("enter the amount: "))
            if(balance[ind]<amount_withdraw):
                print("insufficient amount")
            else:
                balance[ind]=balance[ind]-amount_withdraw
                print("balance after withdrawal: ",balance[ind])
        elif(options==2):
            amount_deposit=int(input("enter the amount: "))
            balance[ind]=balance[ind]+amount_deposit
            print("balance after deposit",balance[ind])
        elif(options==3):
            print("current balance",balance[ind])
        elif(option==4):
            print("visit again")
        else:
            print("invalid option selected")
        break
    elif(ind<len(userName)-1):
        continue
    else:
        print("credentials not matching")
        
    
    
        
    
        
