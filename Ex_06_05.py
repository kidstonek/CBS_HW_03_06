"""
Задача:

Створи клас Library, який міститиме списки книг та авторів.
Реалізуй методи для додавання книг та авторів.
Використовуй ітератор для перебору книг кожного автора.

Також реалізуйте меню для виклику кожної лдосутпної операції

"""

class Library:

    def __init__(self, author=None, authors_books=None):
        self.__content = {}
        self.__author = author
        self.__authors_books = authors_books

    def get_items_from_library(self):
        return self.__content

    def add_items_to_library(self, author, authors_books):
        if not author in self.__content.keys():
            self.__author = author
            self.__authors_books = authors_books
            self.__content[author] = authors_books
        else:
            self.__authors_books = authors_books
            for book in authors_books:
                self.__content[author].append(book)


    def __str__(self):
        return f'{self.__content}'
#


lib = Library()

lib.add_items_to_library("Author1", ['first', 'second', 'black'])
lib.add_items_to_library("Author2", ['pink', 'sonder', 'third'])


print(lib.get_items_from_library())

lib.add_items_to_library("Author2", ['black', 'yellow'])


print(lib)





