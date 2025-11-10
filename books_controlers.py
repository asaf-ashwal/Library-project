import json


class Books_controlers:
    @staticmethod
    def get_db():
        with open("books_DB.json", "r") as file:
            return json.load(file)

    @staticmethod
    def push_db(new_data):
        with open("books_DB.json", "w") as file:
            json.dump(new_data, file)

    def read_one(book_id):
        books = Books_controlers.get_db()
        for b in books:
            if b["ISBN"] == book_id:
                return b
        return None

    def read_all():
        books = Books_controlers.get_db()
        return books

    def creat(book):
        result = Books_controlers.read_one(book['ISBN'])
        if result != None:
            books = Books_controlers.get_db()
            books.append(book)
            Books_controlers.push_db(books)
        else: print('we all reddy hav this book')
        

    def uppdate_avaliable(
        book_id,
    ):
        books = Books_controlers.get_db()
        for b in books:
            if b["ISBN"] == book_id:
                b["is_avaliable"] = not b["is_avaliable"]
                break

        Books_controlers.push_db(books)

    def delete(
        book_id,
    ):
        books = Books_controlers.get_db()
        for b in range(len(books)):
            if books[b]["ISBN"] == book_id:
                del books[b]
                break
        Books_controlers.push_db(books)
