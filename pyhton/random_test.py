class Book:
    def __init__(self, title, category, author, isbn):
        self.title = title
        self.category = category
        self.author = author
        self.isbn = isbn
        self.status = True

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
        
# Library class

default_books = [
    Book("Python Programming", "Programming", "John Doe", "123456"),
    Book("Data Science Basics", "Data Science", "Jane Smith", "789012"),
    Book("A+ Guide to IT Technical Support", "Programming", "", "1-305-26643-9"),
    Book("Elementary Engineering Fracture Mechanics", "Engineering Guide", "David Broek", "978-81-322-0790-0"),
    Book("Fluid Flow Measurement", "Engineering Guide", "Paul j. Lanasa", "978-0-12-409524-3"),
    Book("Vector Mechanics", "Engineering Guide", "Ferdinand P. Beer", "978-981-4577-71-7"),
    Book("Advanced Engineering Mathematics", "Engineering Guide", "Peter v. O'neil", "1-305-63515-9"),
    Book("Beginning DirectX", "Programming", "Wendy Jones", "1-4354-5895-8"),
    Book("Using Information Technology", "Programming", "Williams Sawyer", "978-1-259-25566-3"),
    Book("Discrete Mathematics", "Mathematics", "", "978-1-68095-575-0"),
    Book("Discrete Mathematics and It's Application", "Mathematics", "", "978-1307428674"),
    Book("Java Programming", "Programming", "Bart Baesens", "978-1-118-73949"),
    Book("Biochemistry", "Science", "Stephen Stoker", "978-971-98-0878-7"),
    Book("Analitical Chemistry", "Science", "Donald M. West", "978-981-4352-69-7"),
    Book("Steel Designer Manual", "Engineering Guide", "Buick Davidson", "978-1-1192-4986-3"),
    # Add more default books as needed
    ]