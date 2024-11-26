class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} издает звук: {self.sound}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "мяу")
        self.color = color

    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) издает звук: {self.sound}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "гав")
        self.color = color

    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) издает звук: {self.sound}")


if __name__ == "__main__":
    # Создаем объекты Cat и Dog
    cat = Cat(name="Кошка", color="черный")
    dog = Dog(name="Собака", color="коричневый")

    # Вызываем метод makesound() для каждого объекта
    cat.makesound()
    dog.makesound()
