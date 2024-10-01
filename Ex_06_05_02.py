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


class Book:
    def __init__(self, book_name):
        self._book_name = book_name

    def __str__(self):
        return self._book_name


class Author:
    def __init__(self, author_name: str):
        self._authors_books = []
        self._author_name = author_name

    def add_books(self, books: Book):
        if books._book_name not in self._authors_books:
            self._authors_books.append(books._book_name)

    def __str__(self):
        return f'Author name is {self._author_name} and he has these book\\s {" , ".join(self._authors_books)}'


class Library:
    def __init__(self):
        self.__content = {}

    def add_items_to_library(self, author: Author):
        self.__content[author._author_name] = author._authors_books

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self.__content):
            raise StopIteration

        my_author = list(self.__content.keys())[self.current_index]
        my_author_books = ', '.join(self.__content[my_author])
        self.current_index += 1
        return f'author {my_author} with books: {my_author_books}'


book1 = Book("first")
book2 = Book("Second")

auth1 = Author("Misha")
auth2 = Author("Valera")


auth1.add_books(book1)
auth1.add_books(book2)
lib = Library()
lib.add_items_to_library(auth1)
lib.add_items_to_library(auth2)

for i in lib:
    print(i)
