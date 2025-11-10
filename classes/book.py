from uuid import uuid4


class Book:
    def __init__(self, title: str, author: str):
        self.title: str = title
        self.author: str = author
        self.ISBN: str = str(uuid4())
        self.is_avaliable: bool = True

    def report(self):
        return self.__dict__

    def __str__(self):
        return f"title: {self.title}. author: {self.author}. ISBN: {self.ISBN}. is avaliable: {self.is_avaliable}"
