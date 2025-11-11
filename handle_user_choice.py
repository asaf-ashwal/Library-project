from classes.book import Book
from classes.user import User
class Handle_user_choice:
    @staticmethod
    def save_book():
        title: str = input('enter title name: ') 
        author: str = input('enter author name: ') 
        return Book(title, author)
    @staticmethod
    def save_user():
        name: str = input('enter your name: ') 
        return User(name)
