"""Завдання 3

Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed)."""

class MyIterator:
    def __init__(self, obj: list):
        self.obj = obj

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        if self.current_index * -1 == len(self.obj) + 1:
            raise StopIteration

        result = self.obj[self.current_index]
        self.current_index -= 1
        return result


if '__main__' == __name__:
    my_iterable_object = [1, 2, 3]

    for char in MyIterator(my_iterable_object):
        print(char)