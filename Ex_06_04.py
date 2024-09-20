"""
Надсилаю задачі до домашки. Вчора не встиг тому якщо не виконаєте на сьогодні перевіримо в понеділок


Завдання 1: Ітератор для розбору словника
Опис завдання:

Напиши ітератор, який буде перебирати словник певної структури. Словник містить категорії товарів,
де кожна категорія — це ключ, а значенням є список товарів у цій категорії. Ітератор повинен повертати
назву категорії та окремо кожен товар з цієї категорії.

products = {
    "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
    "Одяг": ["Футболка", "Джинси", "Куртка"],
    "Книги": ["Роман", "Фентезі", "Наукова література"]
}

очікуваний результат

("Електроніка", "Телефон")
("Електроніка", "Ноутбук")
("Електроніка", "Навушники")
("Одяг", "Футболка")
...

"""

class MyIterator:
    def __init__(self, obj: dict):
        self.obj = obj

    def __iter__(self):
        self.current_index = 0
        self.current_position = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.obj.keys()):
            raise StopIteration

        result = (list(self.obj.keys())[self.current_index], self.obj[list(self.obj.keys())[self.current_index]][self.current_position])
        print(self.current_position)
        if self.current_position  < len(self.obj[list(self.obj.keys())[self.current_index]]):
            if self.current_index < len(list(self.obj.keys())):
                self.current_index += 1
                self.current_position = 0
            else:
                self.current_position += 1
                self.current_index += 1
        print(self.current_position, 'rrr')
        return result


if '__main__' == __name__:

    products = {
        "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
        "Одяг": ["Футболка", "Джинси", "Куртка"],
        "Книги": ["Роман", "Фентезі", "Наукова література"]
    }

    for char in MyIterator(products):
        print(char)

# print((list(products.keys())[0]))
# print(len(products["Електроніка"]))