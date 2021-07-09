from project.library import Library


class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        for books in library.books_available.values():
            if book_name in books:
                self.books.append(book_name)
                library.books_available[author].remove(book_name)
                if self.username in library.rented_books:
                    library.rented_books[self.username][book_name] = days_to_return
                else:
                    library.rented_books[self.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in library.rented_books.items():
            if book_name in books:
                days_left = library.rented_books[user][book_name]
                return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            self.books.remove(book_name)
            del library.rented_books[self.username][book_name]
            library.books_available[author].append(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})


user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
