class Animals:
    def breath(self):
        print("дихає")

    def move(self):
        print("рухається")

    def eat_food(self):
        print("їсть")


class Dogs(Animals):
    pass


class Cat(Animals):
    pass


# створення екземпляру класу
my_dog = Dogs()
# методи
my_dog.breath()
