import json
def read_one(book_id):
    with open("DB.json", "r") as file:
        books = json.load(file)
        return books["books"][book_id]
def read_all():
    with open("DB.json", "r") as file:
        books = json.load(file)
        return books["books"]
    
