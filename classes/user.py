from uuid import uuid4


class User:
    def __init__(self, name: str):
        self.name: str = name
        self.borrowed_books: list = []
        self.id: str = str(uuid4())

    def report(self):
        return self.__dict__



