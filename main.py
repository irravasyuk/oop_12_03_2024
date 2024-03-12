# Завдання 4
#  Створіть клас Car з атрибутами brand (марка
# автомобіля), model (модель) та year (рік випуску).
# Додайте метод start_engine, який виведе повідомлення
# про те, що двигун запущено.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def engine_run(self):
        print("Двигун запущений")

car1 = Car("Tesla", "Model X", 2022 )
car1.engine_run()
