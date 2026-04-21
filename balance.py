from utils import *

def show_bal():
    unique_idd = int(input("Enter your Unique User Id: "))
    
    if unique_idd in unique_user_ids:
        i = unique_user_ids.index(unique_idd)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == unique_pins[i]:
            balancee = balances[i]
            print(f"Available Balance in your account is: {balancee}")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")