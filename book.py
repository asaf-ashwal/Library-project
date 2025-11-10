from uuid import uuid4
class Book:
    def __init__(self, titel: str, author: str):
        self.titel: str = titel 
        self.author: str = author 
        self.ISBN: str = str(uuid4())
        self.is_avaliable: bool = True

    def __str__(self):
        return f"titel: {self.titel}. author: {self.author}. ISBN: {self.ISBN}. is avaliable: {self.is_avaliable}"
    

    
