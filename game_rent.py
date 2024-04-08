import os

games = {"Donkey Kong": {"price": 10.00, "copy": 10},
        "Tetris": {"price": 0.99, "copy": 150},
        "Resident Evil": {"price": 14.99, "copy": 15},
        }

accounts = {"russell": {'password':'marcelo', 'rented':['Resident Evil']}}

logged_in = None
wallet = None
cart = {}

def register():
    while True:
        username = input("Enter username(leave blank to return):")
        if username =="":
            os.system('cls')
            return entry_menu()
        if username in accounts.keys():
            print("Username already taken. Try again")
        if username not in accounts.keys():
            break
   
    while True:
        password = input("Enter password(must be more than 5 characters): ")
        if len(password) >= 5:
            accounts.update({username: {'password': password, 'rented': None}})
            print("=========================")
            print("---Account registered---")
            print("=========================")
            print("Press Enter to continue and Log in.. ")
            input()
            os.system('cls')
            return
        else:
            print("Password must be 5 or more characters")

def log_in():
    global logged_in
    while True:
        username = input("Enter username(leave blank to return): ")
        if username == "":
            os.system('cls')
            return entry_menu()
        else:
            if username not in accounts.keys():
                print("your username is not registered. Try again")
            elif username in accounts.keys():
                logged_in = username
                while True:
                    password = input("Password: ")
                    if accounts[username]['password'] == password:
                        print("=========================")
                        print("---Sign in Successful---")
                        print("=========================")
                        print("Press Enter to conitnue...")
                        input()
                        os.system('cls')
                        return main_menu()
                   
                    else:
                        print(f"Incorrect password for {username}.")

def entry_menu():
    while True:
        print("===========================")
        print ("{1} Log in\n{2} Register")
        try:
            first_menu = int(input("Enter your choice: "))
            if first_menu == 1:
                log_in()
                break              
            elif first_menu == 2:
                register()
            else:
                print("Please enter 1 or 2 only")
        except ValueError:
            print("Please enter 1 or 2 only")
           
def balance():
    global wallet
    while True:
        try:
            wallet = int(input("How much is your budget: $"))
            if  wallet <=0:
                print("PLease enter a reasonable ammount..")
            else: game_choice()
        except ValueError:
                print("PLease enter a reasonable ammount..")

def  game_choice():
    global wallet
    games_keys = list(games.keys())
    i=1
    while True:
        try:
            print("========================")
            for items in games:
                print(f"[{i}]{items}: ${games[items]['price']} || Copies: {games[items]['copy']}")
                i += 1
            print("========================")
            print(f"Balance: ${wallet}")
            shopping = int(input("what item would you like to buy: "))
            shopping -= 1
            shopping = games_keys[shopping]
            while True:
                print("===========================")
                print(f"cart = [{shopping}]")
                item_amount = int(input("How many copies?: "))
                if games[shopping]['copy'] >= item_amount:
                    cart[shopping] = [games[shopping]['price'],item_amount]
                    wallet = wallet - (cart[shopping][0] * cart[shopping][1])
                    print(f"Added {item_amount} {shopping} to the cart")
                    print(cart)
                    add_choice= int(input("[1]Yes\n[2]No\nWould you like to add more?: "))
                    if add_choice ==1:
                        os.system('cls')
                        return game_choice()
                    elif add_choice == 2:
                        os.system('cls')
                        purchase()
                    else:
                        print("Please input only  '1' or '2'. Try again.")
                else:
                    print("We don't have that many of that game")
                    print("Press any key to coninue..")
                    input()
                    os.system('cls')
        except ValueError:
            print("Please pick only from the given numbers..")
            print("Press any key to coninue..")
            input()
            i=1
            os.system('cls')

def purchase():
    global wallet, cart, logged_in
    total = 0
    cart_keys = list(cart.keys())
    for items in cart_keys:
        total += cart[items][0] * cart[items][1]
    print(f"total: ${round(total, 2)}")
    purchase_decision = int(input("[1]Yes\n[2]No\nWould you like to end your transaction?: "))
    if purchase_decision == 1:
        for item in cart:
            games[item]['copy'] -= cart[item][1]
            if 'rented' not in accounts[logged_in].keys():
                accounts[logged_in]['rented'] = []
            else:
                accounts[logged_in]['rented'].append(item)
        print(f"Your rental game(s) have been updated to {accounts[logged_in]['rented']}")
        print("Press Enter to return to the main menu..")
        input()
        os.system('cls')
        main_menu()
        cart = {}
        wallet -= total
        if wallet < 0:
            print("Insufficient balance")
            wallet += total
            cart = {}
    else:
        print("Transaction cancelled")
       
def main_menu():
    global logged_in
    print("===========================")    
    print(f"Welcome {logged_in}")
    print(f"Rented: {accounts[logged_in]['rented']}")
    if wallet != None:
        print(f"Balance: ${wallet}")
    print("===========================")  
    while True:
        print("{1} Rent\n{2} Return\n{3} Add Game\n{4} Log out")
        try:
            main_choice = int(input("Enter Choice: "))
            if main_choice == 1:
                os.system('cls')
                balance()
            elif main_choice == 2:
                os.system('cls')
                print("not yet finished")#===================================================================================================
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
   
entry_menu()

