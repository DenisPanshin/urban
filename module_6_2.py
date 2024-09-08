class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._color = color
        self._engine_power = engine_power


    def get_model(self):
        return f'Модель: {self._model}''\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}''\n'

    def get_color(self):
        return f'Цвет: {self._color}''\n'

    def print_info(self):
        print(f'{self.get_model()}{self.get_horsepower()}{self.get_color()}Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, *args):
        super().__init__(*args)



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

