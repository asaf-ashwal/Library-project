import json
from controlers.books_controlers import Books_controlers


class Users_controlers:
    @staticmethod
    def get_db():
        with open("DB/users_DB.json", "r") as file:
            return json.load(file)

    @staticmethod
    def push_db(new_data):
        with open("DB/users_DB.json", "w") as file:
            json.dump(new_data, file)

    def read_one(user_id):
        users = Users_controlers.get_db()

        for u in users:
            if u["id"] == user_id:
                return u
        return None

    def read_all():
        users = Users_controlers.get_db()
        return users

    def creat(user):
        resolt = Users_controlers.read_one(user.id)
        if resolt == None:
            users = Users_controlers.get_db()
            users.append(user.report())
            Users_controlers.push_db(users)
        else:
            print("we all reddy hav this user")

    def add_book_to_list(book_id, user_id):
        result = Books_controlers.read_one(book_id)
        if result != None:

            users = Users_controlers.get_db()
            for i in users:
                print(i["id"] == user_id)
                if i["id"] == user_id:
                    i["borrowed_books"].append(book_id)
                    Users_controlers.push_db(users)
                    break
        else:
            print("i didnt find this book")

    def remove_book_to_list(book_id, user_id):

        users = Users_controlers.get_db()
        for i in users:
            if i["id"] == user_id:
                for j in range(len(i["borrowed_books"])):
                    if i["borrowed_books"][j] == book_id:
                        del i["borrowed_books"][j]
                        Users_controlers.push_db(users)
                        break

    def delete(
        book_id,
    ):
        books = Users_controlers.get_db()
        for b in range(len(books)):
            if books[b]["ISBN"] == book_id:
                del books[b]
                break
        Users_controlers.push_db(books)
