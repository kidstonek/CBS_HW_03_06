"""Завдання 1

Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable"""



class MyIterator:
    def __init__(self, obj: str):
        self.obj = obj

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index == len(self.obj):
            raise StopIteration

        result = self.obj[self.current_index]
        self.current_index += 1
        return result


if '__main__' == __name__:
    my_iterable_object = 'мій об\'єкт'

    for char in MyIterator(my_iterable_object):
        print(char)
