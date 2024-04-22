
import os

global_username = None
global_balance = None

accounts = {
    "russell": ['mynewname', 20],
    "marcelo": ['russell', 10]
}

def sign_up():
    global global_username
    while True:
        username = input("Enter username(leave blank to return):")
        if username =="":
            os.system('cls')
            return sign_menu
        if username in accounts.keys():
            print("Username already taken. Try again")
        if username not in accounts.keys():
            break
    
    while True:
        password = input("Enter password(must be more than 5 characters): ")
        if len(password) >= 5:
            accounts.update({username: [password, 0]})
            print("=========================")
            print("---Account registered---")
            print("=========================")
            print("Press Enter to continue and Sign in.. ")
            input()
            os.system('cls')
            return
        else:
            print("Password must be 5 or more characters")

def sign_in():
    global global_balance
    global global_username
    while True:
        username = input("Enter username(leave blank to return): ")
        if username == "":
            os.system('cls')
            sign_menu()
            break
        else: 
            if username not in accounts.keys():
                print("your username is not registered. Try again")
            elif username in accounts.keys():
                global_username = username
                while True:
                    password = input("Password: ")
                    if accounts[username][0] == password:
                        global_balance = float(accounts[username][1])
                        print("=========================")
                        print("---Sign in Successful---")
                        print("=========================")
                        print("Press Enter to conitnue...")
                        input()
                        os.system('cls')
                        return main_menu()
                    
                    else:
                        print(f"Incorrect password for {username}.")
                

def sign_menu():
    while True:
        print ("{1} Sign in\n{2} Sign up")
        try:
            first_menu = int(input("Enter your choice: "))
            if first_menu == 1:
                sign_in() 
                break               
            elif first_menu == 2:
                sign_up()
            else:
                print("Please enter 1 or 2 only")
        except ValueError:
            print("Please enter 1 or 2 only")

def withraw():
    global global_balance
    while True:
        try:
            print("========WITHDRAW=======")
            withdraw_amount = float(input("Amount to withdraw(leave blank to return): "))
            if withdraw_amount == "":
                os.system('cls')
                return main_menu
            if withdraw_amount > global_balance:
                print("---Not enough Balance--")
                print("Press Enter to continue..")
                input()
                os.system('cls')
            elif withdraw_amount <= global_balance:
                global_balance -= withdraw_amount
                print("=======================")
                print("--Withdaw Successful--")
                print("New Balance: ", global_balance)
                print("=======================")
                print("Press Enter to return...")
                input()
                os.system("cls")
                return main_menu() 
                     
        except ValueError:
            print("Please input a Numerical Value")
            print("Press Enter to continue...")
            input()
            os.system("cls")
            
def deposit():
    global global_balance
    while True:
        try:
            print("========DEPOSIT=======")
            deposit_amount = float(input("Amount ot Deposit(leave blank to return): "))
            if deposit_amount == "":
                os.system('cls')
                return main_menu()
            else:
                global_balance += deposit_amount
                print("=======================")
                print("--Deposit Successful--")
                print("New Balance: ", global_balance)
                print("=======================")
                print("Press Enter to return...")
                input()
                os.system("cls")
                return main_menu()                        
        except ValueError:
            print("Please input a Numerical Value")
            print("Press Enter to continue...")
            input()
            os.system("cls")
                
      
def main_menu():
    global global_username
    global global_balance
    print("===========================")    
    print(f"Welcome {global_username}")
    print(f"Balance: ${global_balance}")  
    print("===========================")  
    while True:
        print("{1} Withraw\n{2} Deposit\n{3} Exit")
        try:
            main_choice = int(input("Enter Choice: "))
            if main_choice == 1:
                os.system('cls')
                withraw()
            elif main_choice == 2:
                os.system('cls')
                deposit()
            elif main_choice == 3:
                accounts[global_username][1] = global_balance
                os.system('cls')
                print("=============================")
                print("---Thank you and good bye---")
                print("=============================")
                global_username = None
                global_balance = None
                exit()
            else:
                print("Please enter 1-3 only")
        except ValueError:
            print("Please enter 1-3 only")
        

sign_menu()
