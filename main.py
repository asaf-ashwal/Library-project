from classes.library import Library
from classes.user import User
from classes.book import Book
from .handle_user_choice import Handle_user_choice
if __name__ == '__main__':
    # u1 = User('evyatar')
    # u2 = User('ori')
    # b1 = Book('bereshit','hashem')
    # library1 = Library()
    # library1.add_book(b1)
    # library1.add_user(u1)
    # print(library1.list_available_books())
    # library1.return_book("03078216-ddf2-4382-8425-fc199858b517","35a2c8a3-af4e-46c0-8b63-45f4e8f5cb60")
    # library1.return_book("b1c9995a-f6a7-4144-b6ad-53eb9e56c592","8e086bdd-939b-4e1a-a13c-f62bcea2471f")
    # library1.search_book('hashem')




    library1 = Library()
    my_user: User = ''
    choice = None
    while choice != "7":
        print("1. Add Book\n2. Add User\n3. Borrow Book\n7. Save & Exit: ")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_book: Book = Handle_user_choice.save_book()
            library1.add_book(new_book)
            
        elif choice == "2":
            new_user: User = Handle_user_choice.save_user()
            my_user = new_user
            library1.add_user(new_user)

        elif choice == "3":
            books: list [dict]  = library1.list_available_books()
            print(books)
            book_id: str = input('enter book id: ')
            library1.borrowed_books(my_user.id,book_id)

        elif choice == "4":
            # return book || TO - DO .
            books: list [dict]  = library1.list_available_books()
            print(books)
            book_id: str = input('enter book id: ')
            library1.borrowed_books(my_user.id,book_id)

        elif choice == "7":
        # save data and exit
            break
        else:
            print("Invalid choice, try again.")


