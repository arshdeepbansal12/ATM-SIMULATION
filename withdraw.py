from utils import *

def with_draw():
    unique_idd = int(input("Enter your Unique User Id: "))
    
    if unique_idd in unique_user_ids:
        i = unique_user_ids.index(unique_idd)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == unique_pins[i]:
            withd = int(input("Enter the amount you want to withdraw: "))
            
            if balances[i] >= withd:
                balances[i] -= withd
                transactions[i].append(f"Withdrawn: -₹{withd}")
                print(f"The amount {withd} has been withdrawn from your account")
            else:
                print("Insufficient Balance !!")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")