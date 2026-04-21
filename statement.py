from utils import *

def check_statement():
    unique_idd = int(input("Enter your Unique User Id: "))
    
    if unique_idd in unique_user_ids:
        i = unique_user_ids.index(unique_idd)
        print(f"Greetings Mr. {username[i]}")
        
        unique_pinn = int(input("Enter your PIN: "))
        
        if unique_pinn == unique_pins[i]:
            print("\n--- Bank Statement ---")
            
            
            user_history = transactions[i]
            
           
            if len(user_history) == 0:
                print("No recent transactions.")
            else:
               
                for record in user_history:
                    print(record)
            
            print(f"----------------------")
            print(f"Current Balance: ₹{balances[i]}\n")
            
        else:
            print("Invalid PIN !!!")
    else:
        print("Invalid Unique User ID")