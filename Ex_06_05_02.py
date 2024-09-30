"""

Завдання 2: Бібліотека книг та авторів
Опис завдання:

Створи класову структуру для керування бібліотекою. Має бути два основних класи: Author та Book.
Клас Author представляє автора з його іменем і списком книг,
а клас Book представляє окрему книгу з її назвою.

Додатково, бібліотека повинна використовувати ітератори для зручної навігації та перегляду книг кожного автора.

Задача:

Створи клас Library, який міститиме списки книг та авторів.
Реалізуй методи для додавання книг та авторів.
Використовуй ітератор для перебору книг кожного автора.

Також реалізуйте меню для виклуку кожної лдосутпної операц

"""

class Author:
    def __init__(self, author_name: str):
        self.__author_name = author_name


class Book:
    def __init__(self, book_name):
        self.__book_name = book_name


class Library:
    def __init__(self, author = Author, authors_books= Book):
        self.__content = {}
        self.__author = author
        self.__authors_books = authors_books

    def add_items_to_library(self, author, authors_books):
        if not author in self.__content.keys():
            self.__author = author
            self.__authors_books = authors_books
            self.__content[author] = authors_books
        else:
            self.__authors_books = authors_books
            for book in authors_books:
                self.__content[author].append(book)
