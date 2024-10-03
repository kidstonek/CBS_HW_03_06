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
    def __init__(self):
        self._whole_books = []

    def add_books(self, new_book: str):
        self.__book = new_book
        if self.__book not in self._whole_books:
            self._whole_books.append(self.__book)

    def __str__(self):
        return ', '.join(self._whole_books)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self._whole_books):
            raise StopIteration

        result = self._whole_books[self.current_index]
        self.current_index += 1
        return result


class Author:
    def __init__(self, author_name: str):
        self._authors_books = []
        self._author_name = author_name

    def add_books(self, books: Book):
        self._authors_books = books

    def __str__(self):
        return f"Author name is {self._author_name} he has these books: {' , '.join(self._authors_books)}"

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self._authors_books._whole_books):
            raise StopIteration

        result = self._authors_books._whole_books[self.current_index]
        self.current_index += 1
        return result


class Library:
    def __init__(self):
        self._content = {}

    def add_items_to_library(self, author: Author):
        self._content[author._author_name] = author._authors_books

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if len(self._content) == 0:
            print("The library is empty")
            raise StopIteration
        if self.current_index == len(self._content):
            raise StopIteration

        my_author = list(self._content.keys())[self.current_index]
        my_author_books = ', '.join(self._content[my_author])
        self.current_index += 1
        return f'author {my_author} with books: {my_author_books}'


if __name__ == "__main__":
    my_book = Book()

    my_book.add_books('author_1')
    my_book.add_books('author_3')
    my_book.add_books('author_5')
    my_book.add_books('author_3')

    ath1 = Author('Oleg')
    ath1.add_books(my_book)

    my_book2 = Book()

    my_book2.add_books('some_1')
    my_book2.add_books('some_2')
    my_book2.add_books('some_3')

    ath2 = Author('Igor')
    ath2.add_books(my_book2)

    lib = Library()
    # lib.add_items_to_library(ath1)
    # lib.add_items_to_library(ath2)


def show_library(info: Library):   # for i in lib:
    for item in info:
        print(item)


while True:
    print("choose what to do:\n1) Show library:\n2) Add element to library\n3) Show all Books\n4) Show all Authors")
    option = input('choose options: ')
    if option == '1':
        print()
        show_library(lib)
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        pass
    else:
        print('end!')
        break
