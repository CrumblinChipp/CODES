import os

grocery = {
    "tissue": [2.99, 3, True], 
    "vegetable": [5.99, 5, True],
    "meat": [6.99, 7, False],
    "milk":  [1.99, 4, True],
    "cheese" :[7.99, 1, True]
}

cart = {
    
}
def buy():
    grocery_keys = list(grocery.keys())
    i=1
    while True:
        try:
            print("========================")
            for items in grocery:
                print(f"[{i}]{items}: ${grocery[items][0]}") 
                i += 1
            print("========================")
            shopping = int(input("what item would you like to buy: "))
            shopping -= 1
            shopping = grocery_keys[shopping]
            if grocery[shopping][2] == False:
                print("This item is not available")
                print("Press any key to coninue..")
                input()
                i=1
                os.system('cls')
            else: 
                print("This item is available")
                
                while True:
                    print("===========================")
                    print(f"cart = [{shopping}]")
                    item_amount = int(input("How many  of that item do you want?: "))
                    if grocery[shopping][1] >= item_amount:
                        print(f"Added {item_amount} {shopping} to the cart")
                        cart[shopping] = [grocery[shopping][0],item_amount]
                        print(cart)
                        add_choice= int(input("[1]Yes\n[2]No\nWould you like to add more?"))
                        if add_choice ==1:
                            os.system('cls')
                            return buy()
                        elif add_choice == 2:
                            break
                        else:
                            print("Please input only  '1' or '2'. Try again.")
                    else:
                        print("We don't have that many of that item")
                        print("Press any key to coninue..")
                        input()
                        os.system('cls')
        except ValueError:
            print("Please pick only from the given numbers..")
            print("Press any key to coninue..")
            input()
            i=1
            os.system('cls')
        except:
            if shopping > 5:
                print(("Please pick only from the given numbers.."))
                print("Press any key to coninue..")
                input()
                i=1
                os.system('cls')


buy()
