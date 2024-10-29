import queue
import random
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        second = random.randint(3, 10)
        sleep(second)


class Cafe:
    queue = queue.Queue()

    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in guests:
            for j in self.tables:
                my_list = [i.guest for i in self.tables]
                if not None in my_list:
                    self.queue.put(i.name)
                    print(f'{i.name} в очереди')
                    break
                if j.guest is None:
                    j.guest = i.name
                    i.start()
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    break
                elif j.guest:
                    continue

    def discuss_guests(self):
        while not self.queue.empty():
            for i in self.tables:
                if i.guest:
                    print(f'{i.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {i.number} свободен')
                    i.guest = None
                if not self.queue.empty():
                    for j in self.tables:
                        if j.guest is None:
                            j.guest = self.queue.get()
                            print(f'{j.guest} вышел(-ла) из очереди и сел(-а) за стол номер {j.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
