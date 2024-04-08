import os
accounts = {'librarian': {'password': 'librarian_admin', 'books_burrowed': []},
            'student1': {'password': 'student1_pass', 'books_burrowed': ['Biochemistry']}}

books = {"Python Programming": {'Category':"Programming", 'author':"John Doe", 'isbn':"123456", 'status': True},
        "Data Science Basics": {'Category':"Data Science", 'author':"Jane Smith", 'isbn':"789012", 'status': True},
        "A+ Guide to IT Technical Support": {'Category':"Programming", 'author':"", 'isbn':"1-305-26643-9", 'status': True},
        "Elementary Engineering Fracture Mechanics": {'Category':"Engineering Guide", 'author':"David Broek", 'isbn':"978-81-322-0790-0", 'status': True},
        "Fluid Flow Measurement": {'Category':"Engineering Guide", 'author':"Paul j. Lanasa", 'isbn':"978-0-12-409524-3", 'status': True},
        "Vector Mechanics":{'Category': "Engineering Guide", 'author':"Ferdinand P. Beer", 'isbn':"978-981-4577-71-7", 'status': True},
        "Advanced Engineering Mathematics": {'Category': "Engineering Guide", 'author':"Peter v. O'neil", 'isbn': "1-305-63515-9", 'status': True},
        "Beginning DirectX": {'Category': "Programming", 'author': "Wendy Jones", 'isbn':"1-4354-5895-8", 'status': True},
        "Using Information Technology":{'Category': "Programming", 'author':"Williams Sawyer", 'isbn':"978-1-259-25566-3", 'status': True},
        "Discrete Mathematics": {'Category': "Mathematics", 'author': "", 'isbn':"978-1-68095-575-0", 'status': True}, 
        "Discrete Mathematics and It's Application": {'Category': "Mathematics", 'author': "", 'isbn': "978-1307428674", 'status': True},
        "Java Programming": {'Category': "Programming", 'author':"Bart Baesens", 'isbn':"978-1-118-73949", 'status': True},
        "Biochemistry":{'Category': "Science", 'author':"Stephen Stoker", 'isbn':"978-971-98-0878-7", 'status': False},
        "Analitical Chemistry": {'Category': "Science", 'author':"Donald M. West", 'isbn':"978-981-4352-69-7", 'status': True},
        "Steel Designer Manual":{'Category': "Engineering Guide", 'author': "Buick Davidson", 'isbn':"978-1-1192-4986-3", 'status': True}
}

logged_in = 'student1'

def role():
    global logged_in
    while True:
        print("\t===========================================")
        role_choice = input("\t\t\t[A]Librarian\n\t\t\t[B]Student\n\t\t\tPick your role[A or B]: ").lower()
        if role_choice == 'a':
            while True:
                print("===========================================")
                username = input("Enter username(leave blank to return): ").lower()
                if username == 'librarian':
                    password = input("Enter password: ")
                    if password == accounts['librarian']['password']:
                        print("Log in successful..")
                        print("Press ENTER to continue..")
                        input()
                        os.system('cls')
                        admin_menu()
                        break
                    else:
                        os.system('cls')
                        print("\t\tWRONG PASSWORD")
                elif username == "":
                    os.system('cls')
                    return role()
                else: 
                    os.system('cls')
                    print("\t\tWRONG USERNAME")
        elif role_choice =='b':
            while True:
                print("===========================================")
                username = input("Enter username(leave blank to return): ").lower()
                if username == 'student1':
                    password = input("Enter password: ")
                    if password == accounts['student1']['password']:
                        print("Log in successful..")
                        print("Press ENTER to continue..")
                        input()
                        logged_in = username
                        os.system('cls')
                        student_menu()
                        break
                    else:
                        os.system('cls')
                        print("\t\tWRONG PASSWORD")
                elif username == "":
                    os.system('cls')
                    return role()
                else: 
                    os.system('cls')
                    print("\t\tWRONG USERNAME")

        else: 
            os.system('cls')
            print("input only the choices Below.")

def admin_menu():
    print("\t===========================================")
    print("\t\t\tWelcome Librarian~")
    while True: 
        print("\t===========================================")
        admin_choice = input("\t\t\t[A]Browse Books\n\t\t\t[B]Edit Book\n\t\t\t[C]Add Book\n\t\t\t[D]Remove Book\n\t\t\t[E]Exit\n\t\t\tPick your action: ").lower()
        if admin_choice == 'a':
            print("Continue to browse option")
        elif admin_choice == 'b':
            print("continue to Edit option")
        elif admin_choice == 'c':
            print("continue to Add option")
        elif admin_choice == 'd':
            print("continue to Remove option")
        elif admin_choice == 'e':
            print("continue to Exit option")
        else: 
            os.system('cls')
            print("\t\tinput only the choices Below.")

def student_menu():
    global logged_in
    print("\t===========================================")
    print("\t\t\tWelcome Student1~")
    if accounts['student1']['books_burrowed'] != None:
        print("\t\t\t",accounts['student1']['books_burrowed'])
    while True: 
        print("\t===========================================")
        admin_choice = input("\t\t\t[A]Browse Books\n\t\t\t[B]Burrow Book\n\t\t\t[C]Return Book\n\t\t\t[D]Exit\n\t\t\tPick your action: ").lower()
        if admin_choice == 'a':
            os.system('cls')
            browse_menu()
        elif admin_choice == 'b':
            burrow_book()
        elif admin_choice == 'c':
            print("continue to Return option")
        elif admin_choice == 'd':
            print("continue to Exit option")
        else: 
            os.system('cls')
            print("\t\tinput only the choices Below.")
    
def browse_menu():
    while True:
        print("\t\t===========================================")
        browse_choice = input("\t\t\t[A]Display All Books\n\t\t\t[B]Browse by Category\n\t\t\t[C]Search: ").lower()
        if browse_choice == "":
            return
        elif browse_choice == 'a':
            os.system('cls')
            display_all()
        elif browse_choice == 'b':
            os.system('cls')
            category_display()
        elif browse_choice == 'c':
            os.system('cls')
            search_engine()
        else:
            print("Enter only on the choices below")
        
def display_all():
    book_title = list(books.keys())
    for title in book_title:
        print("===========================================")
        print("Title: ", title)
        print("Category: ", books[title]["Category"])
        print("Author: ", books[title]["author"])
        print("ISBN: ", books[title]["isbn"])
    while True: 
        print("===========================================")
        admin_choice = input("[A]Burrow Book\n[B] Return\nPick your action: ").lower()
        if admin_choice == 'a':
            os.system('cls')
            burrow_book()
        elif admin_choice == 'b':
            return student_menu()
        else: 
            os.system('cls')
            print("input only the choices Below.")
    
def category_display():
    category_list = ['Programming', 'Data Science', 'Engineering Guide', 'Mathematics', 'Science']
    while True: 
        print("\t===========================================")
        print("\t\t[A] Programming \n\t\t[B] Data Science \n\t\t[C] Engineering Guide \n\t\t[D]Mathematics \n\t\t[E] Science")
        category_choice = input("\t\tEnter your desired CATEGORY: ").lower()
        category_prime = None
        if category_choice == 'a':
            category_prime = category_list[0]
            for book_key in books:
                if books[book_key]['Category'] == category_prime:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
            return student_menu()
        elif category_choice == 'b':
            category_prime = category_list[1]
            for book_key in books:
                if books[book_key]['Category'] == category_prime:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
            return student_menu()
        elif category_choice == 'c':
            category_prime = category_list[2]
            for book_key in books:
                if books[book_key]['Category'] == category_prime:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
            return student_menu()
        elif category_choice == 'd':
            category_prime = category_list[3]
            for book_key in books:
                if books[book_key]['Category'] == category_prime:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
            return student_menu()
        elif category_choice == 'e':
            category_prime = category_list[4]
            for book_key in books:
                if books[book_key]['Category'] == category_prime:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
            return student_menu()
        else:
            os.system('cls')
            print("Enter only the choices below..")
        while True: 
            print("===========================================")
            admin_choice = input("[A]Burrow Book\n[B] Return\nPick your action: ").lower()
            if admin_choice == 'a':
                os.system('cls')
                burrow_book()
            elif admin_choice == 'b':
                return student_menu()
            else: 
                os.system('cls')
                print("input only the choices Below.")

def search_engine():
    print("===========================================")
    print("You may search by entering the book ISBN or Title")
    search_item = input("ENTER: ")
    for book_key in books:
        if books[book_key]['isbn'] == search_item or book_key.lower() == search_item:
            print("===========================================")
            print("Title: ", book_key)
            print("Category: ", books[book_key]['Category'])
            print("Author: ", books[book_key]["author"])
            print("ISBN: ", books[book_key]["isbn"])
            if books[book_key]["status"] == True:
                print("Status: Available")
            else:
                print("Status: Not Avaialable")
        while True: 
            print("===========================================")
            admin_choice = input("[A]Burrow Book\n[B] Return\nPick your action: ").lower()
            if admin_choice == 'a':
                os.system('cls')
                burrow_book()
            elif admin_choice == 'b':
                return student_menu()
            else: 
                os.system('cls')
                print("input only the choices Below.")
    
def burrow_book():
    global logged_in
    while True: 
        print("===========================================")
        print("please enter the ISBN or Title of the book you want to burrow")
        search_item = input("ENTER: ")
        for book_key in books:
            if books[book_key]['isbn'] == search_item or book_key.lower() == search_item:
                if books[book_key]["status"] == True: 
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
                    print("Status: Available")
                    print("===========================================")
                    confirm = input("Are you sure you want to burrow this books(Y/N)?").lower()
                    if confirm == 'y':
                        accounts[logged_in]['books_burrowed'].append(book_key)
                        books[book_key]['status'] = False
                        print(accounts[logged_in]['books_burrowed'])
                        print(f"{search_item} Successfully burrowed..")
                        print("Press ENTER to return..")
                        input()
                        os.system('cls')
                        return student_menu()
                    elif confirm == 'n':
                        return student_menu()
                    else:
                        print("something went wrong")
                else:
                    print("the book is currently not Available")

def return_book():
    global logged_in
    while True: 
        print("===========================================")
        print(accounts[logged_in]['books_burrowed'])
        print("please enter the 'Title' of the book you want to Return")
        search_item = input("ENTER: ")
        if search_item in accounts[logged_in]['books_burrowed']:
            choice = input(f"Are you sure you want to return{search_item}(Y/N): ").lower()
            if choice == 'y':
                accounts[logged_in]['books_burrowed'].remove(search_item)
                books[search_item]['status'] = True
                print(accounts[logged_in]['books_burrowed'])
                print(f"{search_item} Successfully Returned..")
                print("Press ENTER to return..")
                input()
                os.system('cls')
                return student_menu()
            elif choice == 'n':
                print("goods")
            else:
                print("something went wrong")
        else:
            print("The book wasnt in your burrowed list")

return_book()