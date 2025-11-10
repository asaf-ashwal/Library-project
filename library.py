from user import User
from book import Book 

class Library:
    def __init__(self):
        self.list_of_users: list = []
        self.list_of_books: list = []

    def add_book(self, book: Book):
        if(type(book) == Book):
            self.list_of_books.append(book)
        # להוסיף לדאטה בייס את הספר
        else: 
            print("The book doesn't exist in the library!") 

    def add_user(self, user: User):
        if(type(user) == User):
            self.list_of_books.append(user)
        else: 
            print("Invalid user!")

    def borrowed_books(self, user_id: str, book_isbn:str):
        self.user_id: str = user_id
        self.book_isbn: str = book_isbn 
        if self.book_isbn in self.list_of_books:
            
            # if self.list_of_books[book_isbn][is_available] == True:
            #     # self.list_of_users[user_id][] 
                pass
        
