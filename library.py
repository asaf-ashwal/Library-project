class Library:
    def __init__(self):
        self.list_of_users: list = []
        self.list_of_books: list = []

    def add_book(self, book):
        # if(type(book) == Book)
        self.list_of_books.append(book.ISBN)
        # else: return 'ספר לא חוקי'

    def add_user(self, user):
        # if(type(user) == User)
        self.list_of_books.append(user.id)
        # else: return 'משתמש לא חוקי'

    def borrowed_books(self, user_id, book_isbn):
        book = 'b'
        user = 'u'
        
