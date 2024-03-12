# Завдання 2
#  Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Площа кола - {3.14 * self.radius**2}")

circle = Circle(3)
circle.area()


