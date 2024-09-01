from functools import total_ordering


@total_ordering
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.houses_history.append(args[0])
        return obj
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return f'Невозможно сравнить {other} с {self}'

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return f'Невозможно сравнить {other} с {self}'

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        else:
            return f'Невозможно сложить {other} с {self}'

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, other + self.number_of_floors)
        else:
            return f'Невозможно сложить {other} с {self}'

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            return f'Невозможно сложить {other} с {self}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
