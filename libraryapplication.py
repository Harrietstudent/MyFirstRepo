class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.members = []
        self.books = []
        self.users = []
        self.reports = []

    def add_member(self, member):
        self.members.append(member)

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def generate_report(self, report):
        self.reports.append(report)


class User:
    def __init__(self, id, first_name, last_name, username, password_hash):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password_hash = password_hash


class Staff(User):
    def __init__(self, id, first_name, last_name, username, password_hash, role, access_level):
        super().__init__(id, first_name, last_name, username, password_hash)
        self.role = role
        self.access_level = access_level

    def generate_report(self, library, report):
        library.generate_report(report)


class Member(User):
    def __init__(self, id, first_name, last_name, username, password_hash):
        super().__init__(id, first_name, last_name, username, password_hash)
        self.reservations = []
        self.loans = []

    def borrow_book(self, book_loan):
        if len(self.loans) < 2:
            self.loans.append(book_loan)
            print(f"Book {book_loan.book.title} borrowed by {self.first_name}.")
        else:
            print(f"Cannot borrow more than 2 books at a time.")

    def reserve_book(self, book_reservation):
        self.reservations.append(book_reservation)
        print(f"Book {book_reservation.isbn} reserved by {self.first_name}.")


class Report:
    def __init__(self, id, generated_by, reservations, loans):
        self.id = id
        self.generated_by = generated_by
        self.reservations = reservations
        self.loans = loans


class BookReservation:
    def __init__(self, id, member, isbn, reservation_date):
        self.id = id
        self.member = member
        self.isbn = isbn
        self.reservation_date = reservation_date


class BookLoan:
    def __init__(self, id, member, book, due_date):
        self.id = id
        self.member = member
        self.book = book
        self.due_date = due_date


class BookISBN:
    def __init__(self, id, isbn):
        self.id = id
        self.isbn = isbn


class PhysicalBook(BookISBN):
    def __init__(self, isbn, title, author, genre):
        super().__init__(id=None, isbn=isbn)
        self.title = title
        self.author = author
        self.genre = genre





# Create a library
my_library = Library(name="OurLibraryTool", location="Melbourne, VIC")

# Create some books
book1 = PhysicalBook(isbn="978-3-16-148410-0", title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
book2 = PhysicalBook(isbn="978-0-7432-7356-5", title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction")

# Add books to library
my_library.add_book(book1)
my_library.add_book(book2)

# Create members and staff
member1 = Member(id=1, first_name="John", last_name="Doe", username="johndoe", password_hash="hash123")
staff1 = Staff(id=101, first_name="Alice", last_name="Smith", username="alicesmith", password_hash="hashadmin", role="Admin", access_level="High")

# Add users to library
my_library.add_member(member1)
my_library.add_user(staff1)

# Member borrows a book
loan1 = BookLoan(id=1, member=member1, book=book1, due_date="2024-09-20")
member1.borrow_book(loan1)

# Staff generates a report
report = Report(id=1, generated_by=staff1, reservations=[], loans=[loan1])
staff1.generate_report(my_library, report)
