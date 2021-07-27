class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
