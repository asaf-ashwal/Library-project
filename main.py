from library import Library
from user import User
from book import Book
if __name__ == '__main__':
    u1 = User('evyatar')
    u2 = User('ori')
    b1 = Book('bereshit','hashem')
    print(b1.report())
    library1 = Library()
    # library1.add_book(b1)
    # library1.add_user(u1)
     # library1.list_available_books()
    # library1.return_book("03078216-ddf2-4382-8425-fc199858b517","35a2c8a3-af4e-46c0-8b63-45f4e8f5cb60")
    # library1.borrowed_books("03078216-ddf2-4382-8425-fc199858b517","35a2c8a3-af4e-46c0-8b63-45f4e8f5cb60")
    library1.search_book('hashem')


