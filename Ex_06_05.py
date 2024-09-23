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

    def __str__(self):
        return f'{self.__content}'


def info():
    print('\n1 for show library\n2 for add\n0 for exit')


def show_lib():
    for books in lib:
        print(books)


def add_items():
    author = input("Please provide the name of the author: ")
    books = []
    books_number = int(input("How many books you want to add?: "))
    for book_num in range(books_number):
        book = input("Provide the name of the book: ")
        books.append(book)
    lib.add_items_to_library(author, books)


if '__main__' == __name__:
    lib = Library()
    lib.add_items_to_library("Author1", ['first', 'second', 'black'])
    lib.add_items_to_library("Author2", ['pink', 'sonder', 'third'])
    lib.add_items_to_library("Author2", ['black', 'yellow'])
    while True:
        info()
        user_input = input("make your choose: ")
        match user_input:
            case '1':
                show_lib()
            case '2':
                add_items()
            case '0':
                break
