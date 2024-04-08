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
        "Biochemistry":{'Category': "Science", 'author':"Stephen Stoker", 'isbn':"978-971-98-0878-7", 'status': True},
        "Analitical Chemistry": {'Category': "Science", 'author':"Donald M. West", 'isbn':"978-981-4352-69-7", 'status': True},
        "Steel Designer Manual":{'Category': "Engineering Guide", 'author': "Buick Davidson", 'isbn':"978-1-1192-4986-3", 'status': True}
}

logged_in = 'student1'

while True: 
    print("===========================================")
    print(accounts[logged_in]['books_burrowed'])
    print("please enter the 'Title' of the book you want to Return")
    search_item = input("ENTER: ")

    if search_item in [book.lower() for book in accounts[logged_in]["books_burrowed"]]:
        choice = input(f"Are you sure you want to return{search_item}(Y/N): ").lower()
        if choice == 'y':
            accounts[logged_in]['books_burrowed'].remove(search_item)
            books[search_item]['status'] = True
            print(accounts[logged_in]['books_burrowed'])
            print(f"{search_item} Successfully Returned..")
            print("Press ENTER to return..")
            input()
        elif choice == 'n':
            print("goods")
        else:
            print("something went wrong")
    else:
        print("The book wasnt in your burrowed list")