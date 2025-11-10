from classes.user import User
from classes.book import Book
from controlers.user_controlers import Users_controlers
from controlers.books_controlers import Books_controlers


class Library:
    def __init__(self):
        self.list_of_books: list = []
        self.list_of_users: list = []

    def add_book(self, book: Book):
        if type(book) == Book:
            Books_controlers.creat(book)
            self.list_of_books.append(book.ISBN)

        else:
            print("The book doesn't exist in the library!")

    def add_user(self, user: User):
        if type(user) == User:
            Users_controlers.creat(user)
            self.list_of_books.append(user)
        else:
            print("Invalid user!")

    def borrowed_books(self, user_id: str, book_isbn: str):
        book = Books_controlers.read_one(book_isbn)
        if book != None:
            print("is: ", book)
            if book["is_avaliable"]:
                Users_controlers.add_book_to_list(book_isbn, user_id)
                Books_controlers.uppdate_avaliable(book_isbn)
        else:
            print("this book is un avaliable")

    def return_book(self, user_id: str, book_isbn: str):
        book = Books_controlers.read_one(book_isbn)
        if not book["is_avaliable"]:
            Users_controlers.remove_book_to_list(book_isbn, user_id)
            Books_controlers.uppdate_avaliable(book_isbn)
        else:
            print("this book is avaliable")

    def list_available_books(self):
        books = Books_controlers.read_all()
        av_books = []
        for book in books:
            if book["is_avaliable"]:
                av_books.append(book)
        return av_books

    def search_book(self, search_by):
        books = Books_controlers.read_all()
        result = []
        for book in books:
            if search_by == book["title"] or search_by == book["author"]:
                result.append(book)

        return result
