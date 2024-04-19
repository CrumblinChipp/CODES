import msvcrt, sys, os

accounts = {'librarian': {'password': 'librarian_admin','role': 'admin', 'books_burrowed': []},
            'student1': {'password': 'student1_pass', 'role': "student", 'books_burrowed': ['Biochemistry']}}

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

logged_in = None
role_key = None

def hidden_input(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = ''
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            sys.stdout.write('\n')
            break
        sys.stdout.write('*')
        sys.stdout.flush()
        password += char
    return password

def role(): # ALL FUNCTION ACCOUNTED FOR
    global logged_in, role_key
    while True:
        print("===========================================")
        username = input("Enter username: ")
        password = hidden_input("Enter password: ")
        if password == accounts[username]['password']:
            role_key = accounts[username]['role']
            print("Log in successful..")
            print("Press ENTER to continue..")
            input()
            if role_key == 'admin':
                os.system('cls')
                admin_menu()
            elif role_key == 'student':
                logged_in = username
                os.system('cls')
                student_menu()
        else:
            os.system('cls')
            print("WRONG PASSWORD")

def admin_menu():
    print("===========================================")
    print("Welcome Librarian~")
    while True:
        print("===========================================")
        admin_choice = input("[A]Browse Books\n[B]Edit Book\n[C]Add Book\n[D]Remove Book\n[E]Exit\nPick your action: ").lower()
        if admin_choice == 'a':
            os.system('cls')
            browse_menu()
        elif admin_choice == 'b':
            os.system('cls')
            edit_books()
        elif admin_choice == 'c':
            os.system('cls')
            add_book()
        elif admin_choice == 'd':
            os.system('cls')
            delete_book()
        elif admin_choice == 'e':
            print("===========================================")
            print("Thank you for using our Library System.\n\tHave a Good Day~")
            print("===========================================")
            exit()
        else:
            os.system('cls')
            print("Input only the choices Below.")

def student_menu():
    global logged_in
    while True:
        print("===========================================")
        print(f"Welcome {logged_in}~")
        if accounts['student1']['books_burrowed'] != None:
            print(accounts['student1']['books_burrowed'])
        print("===========================================")
        admin_choice = input("[A]Browse Books\n[B]Burrow Book\n[C]Return Book\n[D]Exit\nPick your action: ").lower()
        if admin_choice == 'a':
            os.system('cls')
            browse_menu()
        elif admin_choice == 'b':
            os.system('cls')
            burrow_book()
        elif admin_choice == 'c':
            os.system('cls')
            return_book()
        elif admin_choice == 'd':
            print("===========================================")
            print("Thank you for using our Library System.\n\tHave a Good Day~")
            print("===========================================")
            exit()
        else:
            os.system('cls')
            print("Input only the choices Below.")
   
def secondary_menu():
    if role_key == 'admin':
        print("===========================================")
        print("Press ENTER to Return to the Main menu..")
        input()
        os.system('cls')
        return
    elif role_key != 'admin':
        while True:
            print("===========================================")
            choice = input("[A] Burrow Book\n[B] Return to Main Menu\nPick your action: ").lower()
            if choice == 'a':
                burrow_book()
            elif choice == 'b':
                os.system('cls')
                return student_menu()
            else:
                os.system('cls')
                print("input only the choices Below.")

def browse_menu(): # ALL FUNCTION ACCOUNTED FOR
    while True:
        print("===========================================")
        print("[A] Display All Books\n[B] Browse by Category\n[C] Search ")
        browse_choice = input("Enter your action(leave blank to return to the Main Menu): ").lower()
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
       
def display_all(): # ALL FUNCTION ACCOUNTED FOR
    global role_key
    book_title = list(books.keys())
    for title in book_title:
        print("===========================================")
        print("Title: ", title)
        print("Category: ", books[title]["Category"])
        print("Author: ", books[title]["author"])
        print("ISBN: ", books[title]["isbn"])
        print ("Status: Available" if books[title]["status"] == True else "Status: Not Available")
    secondary_menu()
     
def category_display(): # ALL FUNCTION ACCOUNTED FOR
    global role_key
    category_list = ['Programming', 'Data Science', 'Engineering Guide', 'Mathematics', 'Science']
    while True:
        try:
            print("===========================================")
            print("[1] Programming \n[2] Data Science \n[3] Engineering Guide \n[4] Mathematics \n[5] Science")
            category_choice = int(input("Enter your desired CATEGORY: "))
            if category_choice >= 1 and category_choice <=  len(category_list):
                category_choice =  category_list[category_choice-1]
                for book_key in books:
                    if books[book_key]['Category'] == category_choice:
                        print("===========================================")
                        print("Title: ", book_key)
                        print("Category: ", books[book_key]['Category'])
                        print("Author: ", books[book_key]["author"])
                        print("ISBN: ", books[book_key]["isbn"])
                        print ("Status: Available" if books[book_key]["status"] == True else "Status: Not Available")
            else:
                os.system('cls')
                print("Enter only the choices below..")
        except Exception:
            print("Enter only from 1-5")
        secondary_menu()

def search_engine(): # ALL FUNCTION ACCOUNTED FOR
    print("===========================================")
    print("--You may search by entering the ISBN or Title of the book you're searching--")
    search_item = input("ENTER: ")
    for book_key in books:
        if books[book_key]['isbn'] == search_item or book_key.lower() == search_item:
            print("===========================================")
            print("Title: ", book_key)
            print("Category: ", books[book_key]['Category'])
            print("Author: ", books[book_key]["author"])
            print("ISBN: ", books[book_key]["isbn"])
            print ("Status: Available" if books[book_key]["status"] == True else "Status: Not Available")
        else:
            print("We do not have this book..")
            print("Press Enter to continue Searching...")
            input()
            os.system('cls')
            search_engine()
    secondary_menu()
   
def burrow_book(): # ALL FUNCTION ACCOUNTED FOR
    global logged_in
    while True:
        print("===========================================")
        print("--Enter the ISBN or Title of the book you want to burrow--")
        search_item = input("ENTER: ")
        for book_key in books:
            if books[book_key]['isbn'] == search_item or book_key.lower() == search_item:
                if books[book_key]["status"] == True:
                    print("===========================================")
                    print("Title: ", book_key)
                    print("Category: ", books[book_key]['Category'])
                    print("Author: ", books[book_key]["author"])
                    print("ISBN: ", books[book_key]["isbn"])
                    print ("Status: Available" if books[book_key]["status"] == True else "Status: Not Available")
                    print("===========================================")
                    confirm = input("Are you sure you want to burrow this books(Y/N)?").lower()
                    if confirm == 'y':
                        accounts[logged_in]['books_burrowed'].append(book_key)
                        books[book_key]['status'] = False
                        print(accounts[logged_in]['books_burrowed'])
                        print(f"{accounts[logged_in]['books_burrowed'][-1]} Successfully burrowed..")
                        print("Press ENTER to return..")
                        input()
                        os.system('cls')
                        return student_menu()
                    elif confirm == 'n':
                        os.system('cls')
                        return student_menu()
                    else:
                        print("It’s a Yes or No Question(Y/N)")
                else:
                    print("The book is currently not Available")

def return_book(): # ALL FUNCTION ACCOUNTED FOR
    global logged_in
    while True:
        print("===========================================")
        print(accounts[logged_in]['books_burrowed'])
        print("--Enter the 'Title' of the book you want to Return--")
        search_item = input("ENTER: ")
        if search_item in accounts[logged_in]['books_burrowed']:
            choice = input(f"Are you sure you want to return {search_item} (Y/N): ").lower()
            if choice == 'y':
                accounts[logged_in]['books_burrowed'].remove(search_item)
                if len(accounts[logged_in]['books_burrowed']) == 0:
                    accounts[logged_in]['books_burrowed'] = None
                books[search_item]['status'] = True
                print(accounts[logged_in]['books_burrowed'])
                print(f"{search_item} Successfully Returned..")
                print("Press ENTER to return..")
                input()
                os.system('cls')
                return student_menu()
            elif choice == 'n':
                os.system('cls')
                student_menu()
            else:
                print("It’s a Yes or No Question(Y/N)")
        else:
            print("The book is not in your burrowed list")

def edit_books(): # ALL FUNCTION ACCOUNTED FOR
    book_parts = ['Category', 'author', 'isbn']
    print("===========================================")
    print("Enter the ISBN or Title of the Book you want to Edit")
    search_item = input("ENTER: ")
    for book_key in books:
        if books[book_key]['isbn'] == search_item or book_key.lower() == search_item:
            print("===========================================")
            print("Title: ", book_key)
            print("Category: ", books[book_key]['Category'])
            print("Author: ", books[book_key]["author"])
            print("ISBN: ", books[book_key]["isbn"])
            print ("Status: Available" if books[book_key]["status"] == True else "Status: Not Available")
            try:
                print("===========================================")
                print("[1] Category\n[2] Author\n[3] ISBN")
                edit_item = int(input("Enter the part the you want to edit on this book: "))
                if edit_item >= 1 and edit_item <= 3:
                    edit_item -=1
                    edit_item = book_parts[edit_item]
                    change_item = input(f"Enter the new {edit_item}: ")
            except Exception:
                print("Enter only from 1-3")
            confirm = input("Are you sure you want to edit this books(Y/N)?").lower()
            if confirm == 'y':
                books[book_key][edit_item] = change_item
                print("===========================================")
                print("Title: ", book_key)
                print("Category: ", books[book_key]['Category'])
                print("Author: ", books[book_key]["author"])
                print("ISBN: ", books[book_key]["isbn"])
                print ("Status: Available" if books[book_key]["status"] == True else "Status: Not Available")
                print("===========================================")
                print("Press ENTER to return..")
                input()
                os.system('cls')
                return admin_menu()
            elif confirm == 'n':
                os.system('cls')
                admin_menu()
            else:
                print("It’s a Yes or No Question(Y/N)")

def add_book(): # ALL FUNCTION ACCOUNTED FOR
    print("===========================================")
    title = input("Enter Title of Book: ")
    category = input("Enter Category: ")
    author = input("Enter Author Name: ")
    isbn = input ("Enter ISBN Number: ")
    print("Title: ", title)
    print("Category: ", category)
    print("Author: ", author)
    print("ISBN: ", isbn)
    print("===========================================")
    confirm = input("Are all information correct(Y/N): ").lower()
    if confirm == 'y':
        books.update({title:{'Category': category, 'author': author, 'isbn': isbn, 'status': True }})
        print("Book successfully added..")
        print("Press ENTER to return to the main menu..")
        input()
        os.system('cls')
        admin_menu()
    elif confirm == 'n':
        admin_menu()
    else:
        print("It’s a Yes or No Question(Y/N)")

def delete_book(): # ALL FUNCTION ACCOUNTED FOR
    print("===========================================")
    print("Enter the ISBN or Title of the Book you want to Remove")
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
                print("Status: Not Available")
        print("===========================================")
        confirm = input(f"Are you sure you want to Remove {book_key}(Y/N)?").lower()
        if confirm == 'y':
            del books[book_key]
            print("The book has been removed from our library")
            print("Press ENTER to return..")
            input()
            os.system('cls')
            return admin_menu()
        elif confirm == 'n':
            os.system('cls')
            admin_menu()
        else:
            print("It’s a Yes or No Question(Y/N)")

role()