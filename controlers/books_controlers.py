from classes.book import Book
import json


class Books_controlers:
    @staticmethod
    def get_db():
        with open("DB/books_DB.json", "r") as file:
            return json.load(file)

    @staticmethod
    def push_db(new_data: str):
        with open("DB/books_DB.json", "w") as file:
            json.dump(new_data, file)

    

    def read_one(book_id: str):
        books = Books_controlers.get_db()
        for b in books:
            if b["ISBN"] == book_id:
                return b
        return None

    def read_all():
        books: list [dict] = Books_controlers.get_db()
        return books

    def creat(book: Book):
        result: dict | None = Books_controlers.read_one(book.ISBN)
        if result == None:
            books: list [dict] = Books_controlers.read_all()
            books.append(book.report())
            Books_controlers.push_db(books)
        else:
            print("we all reddy hav this book")

    def uppdate_avaliable(
        book_id
    ):
        books: list [dict] = Books_controlers.read_all()
        for b in books:
            if b["ISBN"] == book_id:
                b["is_avaliable"] = not b["is_avaliable"]
                Books_controlers.push_db(books)
                return True
        print("we don't have this book")    

        

    def delete(
        book_id: str
    ):
        books: list [dict] = Books_controlers.read_all()
        for b in range(len(books)):
            if books[b]["ISBN"] == book_id:
                del books[b]
                Books_controlers.push_db(books)
                return True
        print("we don't have this book")    

