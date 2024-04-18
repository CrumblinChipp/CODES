class Book:
    def __init__(self, title, category, author, isbn, status):
        self.title = title
        self.category = category
        self.author = author
        self.isbn = isbn
        self.status = status

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_category(self):
        return self.category

    def get_status(self):
        return self.status

    def borrow_book(self):
        self.status = False

    def return_book(self):
        self.status = True 
     
     
default_books = [
    Book("Python Programming", "Programming", "John Doe", "123456",True),
    Book("Data Science Basics", "Data Science", "Jane Smith", "789012", True),
    Book("A+ Guide to IT Technical Support", "Programming", "", "1-305-26643-9", True ),
    Book("Elementary Engineering Fracture Mechanics", "Engineering Guide", "David Broek", "978-81-322-0790-0", True),
    Book("Fluid Flow Measurement", "Engineering Guide", "Paul j. Lanasa", "978-0-12-409524-3", False),
    Book("Vector Mechanics", "Engineering Guide", "Ferdinand P. Beer", "978-981-4577-71-7", False),
    Book("Advanced Engineering Mathematics", "Engineering Guide", "Peter v. O'neil", "1-305-63515-9", False ),
    Book("Beginning DirectX", "Programming", "Wendy Jones", "1-4354-5895-8", True),
    Book("Using Information Technology", "Programming", "Williams Sawyer", "978-1-259-25566-3", True),
    Book("Discrete Mathematics", "Mathematics", "", "978-1-68095-575-0", True),
    Book("Discrete Mathematics and It's Application", "Mathematics", "", "978-1307428674", True),
    Book("Java Programming", "Programming", "Bart Baesens", "978-1-118-73949", True),
    Book("Biochemistry", "Science", "Stephen Stoker", "978-971-98-0878-7", True),
    Book("Analitical Chemistry", "Science", "Donald M. West", "978-981-4352-69-7", True),
    Book("Steel Designer Manual", "Engineering Guide", "Buick Davidson", "978-1-1192-4986-3", False),
    # Add more default books as needed
]
class Display:    
    
    def display_books():
        for books in default_books:
            print("===============================")
            print(f"Title: {books.get_title()}")
            print(f"Category: {books.get_category()}")
            print(f"Author: {books.get_author()}")
            print(f"ISBN: {books.get_isbn()}")
            print(f"Status: Not Available" if books.get_status() == False else " Status: Available")

class Browse:   
    
    def display_all():
        Display.display_books()

    def category_browse():
        category_list = ['Programming', 'Data Science', 'Engineering Guide', 'Mathematics', 'Science']
        while True:
            try:
                print("===========================================")
                print("[1] Programming \n[2] Data Science \n[3] Engineering Guide \n[4] Mathematics \n[5] Science")
                choice = int(input("Enter your desired CATEGORY: "))
                if choice >= 1 and choice <=  len(category_list):
                    choice =  category_list[choice-1]
                    for books in default_books:
                        if books.get_category() == choice:
                            Display.display_books()
                    break
            except Exception:
                print( "something went wrong")
    
    def search_browse():
        while True: 
            print("===========================================")
            print("PLease enter the Title or ISBN of the Book")
            search = input("(Title or ISBN): ")
            for books in default_books:
                if search == books.get_title() or search == books.get_isbn():
                    Display.display_books()
            break

                

Browse.search_browse()
            
            
