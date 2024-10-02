class Book:
    def __init__(self):
        self.__whole_books = []

    def add_books(self, new_book: str):
        self.__book = new_book
        if self.__book not in self.__whole_books:
            self.__whole_books.append(self.__book)

    def __str__(self):
        return ', '.join(self.__whole_books)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self.__whole_books):
            raise StopIteration

        result = self.__whole_books[self.current_index]
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
        if self.current_index == len(self.__whole_books):
            raise StopIteration

        result = self.__whole_books[self.current_index]
        self.current_index += 1
        return result


my_book = Book()

my_book.add_books('1')
my_book.add_books('3')
my_book.add_books('5')
my_book.add_books('3')

ath1 = Author('Oleg')
ath1.add_books(my_book)

my_book2 = Book()

my_book2.add_books('qwe')
my_book2.add_books('rty')
my_book2.add_books('678')

ath2 = Author('Igor')
ath2.add_books(my_book2)

print(ath1, ath2)

