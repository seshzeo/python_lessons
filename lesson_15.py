def task1():
    class Transport(object):
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def print_info(self):
            print(
                f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

    Autobus = Transport("Dodge Caravan", 180, 270000)
    Autobus.print_info()


def task2():
    class Transport(object):
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def print_info(self):
            print(
                f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

    class Autobus(Transport):
        def __init__(self, name, max_speed, mileage, capacity=50):
            super().__init__(name, max_speed, mileage)
            self.capacity = capacity

        def seating_capacity(self, capacity):
            self.capacity = capacity
            return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

    Dodge = Autobus("Dodge Caravan", 180, 270000)
    print(Dodge.seating_capacity(50))


if __name__ == '__main__':
    # task1()
    task2()
