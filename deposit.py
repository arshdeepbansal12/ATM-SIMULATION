from utils import *

def deposits():
    unique_idd = int(input("Enter your Unique User Id: "))
    
    # Check if the ID exists in the list
    if unique_idd in unique_user_ids:
        # Get the exact index of the user
        i = unique_user_ids.index(unique_idd)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        # Check the PIN at that exact same index
        if unique_pinn == unique_pins[i]:
            depo = int(input("Enter the amount you want to deposit: "))
            balances[i] += depo
            transactions[i].append(f"Deposited: +₹{depo}")

            print(f"The amount {depo} has been deposited to your account")
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")