import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def play(self):
        self.hunger += 1
        self.energy -= 2
        return f"{self.name} грає."

    def sleep(self):
        self.energy += 2
        return f"{self.name} спить."

    def eat(self):
        self.hunger -= 2
        return f"{self.name} їсть."

    def __str__(self):
        return f"{self.name}: Голод - {self.hunger}, Енергія - {self.energy}"

murka = Pet(name="Murka")

print(murka)

print(murka.play())

print(murka.eat())

print(murka.sleep())

print(murka)
