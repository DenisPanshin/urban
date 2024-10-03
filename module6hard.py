class Figure:
    sides_count = 0

    def __init__(self, color, sides, filed=True):
        self.__color = color
        self.__sides = sides
        self.filed = filed

    @property
    def set_color(self):
        return list(self.__color)

    @staticmethod
    def _is_valid_color(r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    @set_color.setter
    def set_color(self, value):
        r, g, b = value
        if self._is_valid_color(r, g, b):
            self.__color = value

    def _is_valid_side(self, *args):
        count = 0
        for i in args:
            if isinstance(i, int) and i > 0 and self.sides_count:
                count += 1
        if count == len(args):
            return True
        else:
            return False

    @property
    def set_sides(self):
        return self.__sides

    def __len__(self):
        return self.__sides

    @set_sides.setter
    def set_sides(self, new_sides):
        if isinstance(new_sides, tuple):
            list_ = [i for i in new_sides]
            if len(list_) == self.sides_count:
                self.__sides = list_

        else:
            if 1 == self.sides_count:
                self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filed=True):
        super().__init__(color, sides, filed)
        self.__radius = sides / 2 * 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.set_sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides, filed=True):
        super().__init__(color, [sides] * self.sides_count, filed)

    def get_volume(self):
        return (self.sides_count / 2) ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color = (55, 66, 77)  # Изменится
print(circle1.set_color)
cube1.set_color = (300, 70, 15)  # Не изменится
print(cube1.set_color)

# Проверка на изменение сторон:
cube1.set_sides = (5, 3, 12, 4, 5)  # Не изменится
print(cube1.set_sides)
circle1.set_sides = (15)  # Изменится
print(circle1.set_sides)

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(int(cube1.get_volume()))
